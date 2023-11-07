from array import *
from params import *
from logic import AND, OR, NOT, BUFF, NAND, NOR, MAJ3, MAJ5, NMAJ3, NMAJ5, WRITE, READ
import MTJ as mtj

dest_mtj = mtj.MTJ(False, 0)
src1_mtj = mtj.MTJ(False, 0)
src2_mtj = mtj.MTJ(False, 0)
active_tiles = 0x0000
data_size = 0
current_layer = 0
current_cap_energy = CAP_ENERGY
time = 0
energy = 0
checkpoints = 0
repeat_time = 0
repeat_energy = 0
charging_time = 0
pamb = 100 # (uW)

def update_pamb(new_pamb):
    global pamb
    pamb = new_pamb

def time_elapsed():
    global time, charging_time
    print(time+charging_time)
    if (time+charging_time >= APP_TIME):
        return True
    return False

def mc_read():
    return MC_READ_TIME, MC_READ_ENERGY
def mc_write():
    return MC_WRITE_TIME, MC_WRITE_ENERGY
def mc_decode():
    return MC_DECODE_TIME, MC_DECODE_ENERGY
def mc_execute():
    return MC_EXECUTE_TIME, MC_EXECUTE_ENERGY

def set_cells(op):
    global dest_mtj, src1_mtj, src2_mtj
    dest_mtj.set_resistance(op.preset_val) 
    src1_mtj.set_voltage(op.min_v)
    src2_mtj.set_voltage(op.min_v)

def capacitor_check(cell_time, cell_energy, energy_factor, primitive):
    global current_cap_energy, checkpoints, repeat_time, repeat_energy, charging_time, pamb
    
    tm = cell_time
    enrg = 0
    iterations = 1
    if primitive == 'MOVE': # We assume that one row at a time is moved from OUT to IN
        enrg = cell_energy * IN_width
        enrg *= active_tiles.bit_count()
        iterations = energy_factor // IN_width
    elif primitive == 'BUFF' or primitive == 'NAND' or primitive == 'OR' or primitive == 'AND' or primitive == 'NOT':  # We assume that CA_width data is processed at a time 
        enrg = cell_energy * WORD_width * CA_width  
        enrg *= active_tiles.bit_count() 
        iterations = energy_factor // (WORD_width * CA_width)     
    else:
        enrg = cell_energy

    
    tm = MC_EXECUTE_TIME
    enrg += MC_EXECUTE_ENERGY# + (MCU_POWER * tm)
    if not CRAM_ONLY:
        enrg += (MCU_POWER * tm)

    for i in range(iterations):
        if current_cap_energy - enrg <= 0:
            checkpoints += 1
            repeat_time += tm
            repeat_energy += enrg
            current_cap_energy = CAP_ENERGY - repeat_energy # Recharge the capacitor.
            charging_time += (CAP_ENERGY/pamb)
        else:
            current_cap_energy -= enrg
            current_cap_energy = min((current_cap_energy + (tm * pamb)), CAP_ENERGY)
            



# The list of the list of functions for each OPCODE
CONFMEM = [
    [], # reserved for 0x00 OPCODE
    [mc_read, mc_decode, mc_write], # tile enable
    [mc_read, mc_decode, mc_write], # tile disable
    [mc_read, mc_decode, mc_write, mc_execute, WRITE], # load to ina
    [mc_read, mc_decode, mc_write, mc_execute, WRITE], # load to inb
    [mc_read, mc_decode, mc_write], # bias enable
    [mc_read, mc_decode, mc_write, mc_execute, READ], # unload from out
    [mc_read, mc_decode, mc_write, mc_execute, BUFF], # move from out to ina
    [mc_read, mc_decode, mc_write, mc_execute, BUFF, NAND], # add
    [mc_read, mc_decode, mc_write, mc_execute, BUFF, NAND], # mult
    [mc_read, mc_decode, mc_write, mc_execute, BUFF, NAND], # relu
    [mc_read, mc_decode, mc_write, mc_execute, BUFF, NOT, AND, OR], # maxpool
    [mc_read, mc_decode, mc_write, mc_execute, BUFF, NAND], # mac
]

def process_HL_instruction(opcode, tileid, size, instline):
    global active_tiles, data_size, current_layer, time, energy, dest_mtj, src1_mtj, src2_mtj
    iterator = 0
    if instline == 1:
        current_layer = 0

    for i in CONFMEM[opcode]:
        t, e, cell_t, cell_e = 0, 0, 0, 0
        multitile = 1
        if (opcode == OPCODE_ina or opcode == OPCODE_inb or opcode == OPCODE_unload) and iterator == 4:
            if opcode == OPCODE_ina: data_size = size
            t, e = i(WORD_width) 
            capacitor_check(t,e,0,'') # We assume that the MC writes\reads to\from CRAM by WORDS
            cell_t, cell_e = i(bits=size)
            t_factor, e_factor = 1, 1
            multitile = 0
        elif (opcode == OPCODE_move) and iterator == 4:
            set_cells(BUFF_OP)
            cell_t, cell_e = i(dest_mtj, src1_mtj)
            t_factor = data_size
            e_factor = WORD_width * data_size
            capacitor_check(cell_t, cell_e, e_factor, 'MOVE') 
        elif opcode == OPCODE_add and iterator > 3:
            if iterator == 4:           # BUFF
                set_cells(BUFF_OP)
                cell_t, cell_e = i(dest_mtj, src1_mtj)
                t_factor = (((ADD_LAYERS[current_layer]/CA_width) * BUFFS_in_ADD) + (2 * ADD_LAYERS[current_layer]/CA_width))
                e_factor = (WORD_width * ADD_LAYERS[current_layer] * BUFFS_in_ADD) + (2 * WORD_width * ADD_LAYERS[current_layer])
                capacitor_check(cell_t, cell_e, e_factor,'BUFF') 
            else:                       # NAND
                set_cells(NAND_OP)
                cell_t, cell_e = i(dest_mtj, src1_mtj, src2_mtj)
                t_factor = (ADD_LAYERS[current_layer]/CA_width) * NANDS_in_ADD
                e_factor = WORD_width * ADD_LAYERS[current_layer] * NANDS_in_ADD 
                capacitor_check(cell_t, cell_e, e_factor, 'NAND')
        elif opcode == OPCODE_mult and iterator > 3:
            if iterator == 4:           # BUFF
                set_cells(BUFF_OP)
                cell_t, cell_e = i(dest_mtj, src1_mtj)
                t_factor = ((MULT_LAYERS[current_layer]/CA_width) * BUFFS_in_MULT + (2 * MULT_LAYERS[current_layer]/CA_width))
                e_factor = (WORD_width * MULT_LAYERS[current_layer] * BUFFS_in_MULT) + (2 * WORD_width * MULT_LAYERS[current_layer])
                capacitor_check(cell_t, cell_e, e_factor, 'BUFF')
            else:                       # NAND
                set_cells(NAND_OP)
                cell_t, cell_e = i(dest_mtj, src1_mtj, src2_mtj)
                t_factor = (MULT_LAYERS[current_layer]/CA_width) * NANDS_in_MULT
                e_factor = WORD_width * MULT_LAYERS[current_layer] * NANDS_in_MULT
                capacitor_check(cell_t, cell_e, e_factor, 'NAND') 
        elif opcode == OPCODE_relu and iterator > 3:
            if iterator == 4:           # BUFF
                set_cells(BUFF_OP)
                cell_t, cell_e = i(dest_mtj, src1_mtj)
                t_factor = ((RELU_LAYERS[current_layer]/CA_width) * BUFFS_in_RELU + (2 * RELU_LAYERS[current_layer]/CA_width))
                e_factor = (WORD_width * RELU_LAYERS[current_layer] * BUFFS_in_RELU) + (2 * WORD_width * RELU_LAYERS[current_layer])
                capacitor_check(cell_t, cell_e, e_factor, 'BUFF')
            else:                       # NAND
                set_cells(NAND_OP)
                cell_t, cell_e = i(dest_mtj, src1_mtj, src2_mtj)
                t_factor = (RELU_LAYERS[current_layer]/CA_width) * NANDS_in_RELU
                e_factor = WORD_width * RELU_LAYERS[current_layer] * NANDS_in_RELU
                capacitor_check(cell_t, cell_e, e_factor, 'NAND')
        elif opcode == OPCODE_maxpool and iterator > 3:
            if iterator == 4:           # BUFF
                set_cells(BUFF_OP)
                cell_t, cell_e = i(dest_mtj, src1_mtj)
                t_factor = (MAXPOOL_LAYERS[current_layer]/CA_width) * 2
                e_factor = WORD_width * MAXPOOL_LAYERS[current_layer] * 2
                capacitor_check(cell_t, cell_e, e_factor, 'BUFF')
            elif iterator == 5:         # NOT
                set_cells(NOT_OP)
                cell_t, cell_e = i(dest_mtj, src1_mtj)
                t_factor = (MAXPOOL_LAYERS[current_layer]/MAXPOOL_vector) * NOTS_in_MAXPOOL
                e_factor = WORD_width * MAXPOOL_LAYERS[current_layer] * NOTS_in_MAXPOOL
                capacitor_check(cell_t, cell_e, e_factor, 'NOT') 
            elif iterator == 6:         # AND
                set_cells(AND_OP)
                cell_t, cell_e = i(dest_mtj, src1_mtj, src2_mtj)
                t_factor = (MAXPOOL_LAYERS[current_layer]/MAXPOOL_vector) * ANDS_in_MAXPOOL
                e_factor = WORD_width * MAXPOOL_LAYERS[current_layer] * ANDS_in_MAXPOOL
                capacitor_check(cell_t, cell_e, e_factor, 'AND') 
            else:                       # OR
                set_cells(OR_OP)
                cell_t, cell_e = i(dest_mtj, src1_mtj, src2_mtj)
                t_factor = (MAXPOOL_LAYERS[current_layer]/MAXPOOL_vector) * ORS_in_MAXPOOL
                e_factor = WORD_width * MAXPOOL_LAYERS[current_layer] * ORS_in_MAXPOOL
                capacitor_check(cell_t, cell_e, e_factor, 'OR') 
        elif opcode == OPCODE_mac and iterator > 3:
            if iterator == 4:           # BUFF
                set_cells(BUFF_OP)
                cell_t, cell_e = i(dest_mtj, src1_mtj)
                t_factor = ((MAC_LAYERS[current_layer]/CA_width) * BUFFS_in_MAC + (2 * MAC_LAYERS[current_layer]/CA_width))
                e_factor = (WORD_width * MAC_LAYERS[current_layer] * BUFFS_in_MAC) + (2 * WORD_width * MAC_LAYERS[current_layer])
                capacitor_check(cell_t, cell_e, e_factor, 'BUFF')
            else:                       # NAND
                set_cells(NAND_OP)
                cell_t, cell_e = i(dest_mtj, src1_mtj, src2_mtj)
                t_factor = (MAC_LAYERS[current_layer]/CA_width) * NANDS_in_MAC
                e_factor = WORD_width * MAC_LAYERS[current_layer] * NANDS_in_MAC
                capacitor_check(cell_t, cell_e, e_factor, 'NAND') 
        elif opcode == OPCODE_enable or opcode == OPCODE_disable:
            cell_t, cell_e = i()
            t_factor, e_factor = 1, 1
            multitile = 0
            capacitor_check(t,e,0,'')
            if opcode == OPCODE_enable and iterator == 0:
                active_tiles |= (1 << tileid) # Set active bit
            elif opcode == OPCODE_disable and iterator == 0:
                active_tiles &= ~(1 << tileid) # Unset active bit
        else: 
            if (opcode == OPCODE_mult or opcode == OPCODE_mac) and iterator == 0:
                current_layer += 1 # Switch to the next NN layer
            cell_t, cell_e = i()
            t_factor, e_factor = 1, 1
            multitile = 0
            capacitor_check(t,e,0,'')
            
        t = cell_t * t_factor
        e = cell_e * e_factor
        if multitile:
            e *= active_tiles.bit_count()
             
            t = MC_EXECUTE_TIME * t_factor
            e += (MC_EXECUTE_ENERGY * e_factor)# + (MCU_POWER * t)
            if not CRAM_ONLY:
                e += (MCU_POWER * t)
        time += t
        energy += e
        iterator += 1

    return time, energy

def print_result():
    print("Ambient Power - %.2f (uW)" % pamb)
    print("Capacitor - %.2f (mF)" % C)

    print("Time - %.3f (ms)" % (time/1000000))
    print("Charching Time - %.3f (ms)" % (charging_time/1000000))
    print("Energy - %.3f (uJ)" % (energy/1000000000))
    print("Remaining Cap Energy - %.3f (uJ)" % (current_cap_energy/1000000000))
    print("Number of Checkpoints - ", checkpoints)
    print("Re-execution Time - %.3f (ms)" % (repeat_time/1000000))
    print("Re-execution Energy - %.3f (uJ)" % (repeat_energy/1000000000))
    print("Re-execution Time Ratio - %.6f (%%)" % ((repeat_time/time)*100))
    print("Re-execution Energy Ratio - %.6f (%%)" % ((repeat_energy/energy)*100))