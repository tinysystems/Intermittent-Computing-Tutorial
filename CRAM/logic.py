from params import *

def AND(dest, src1, src2):
    v = src1.get_voltage()
    check_voltage(v, AND_OP.min_v, AND_OP.max_v)
    dest.set_resistance(AND_OP.preset_val)
    return execute(dest, src1, src2, None, None, None, v)
    
def OR(dest, src1, src2):
    v = src1.get_voltage()
    check_voltage(v, OR_OP.min_v, OR_OP.max_v)
    dest.set_resistance(OR_OP.preset_val)
    return execute(dest, src1, src2, None, None, None, v)

def NOT(dest, src):
    v = src.get_voltage()
    check_voltage(v, NOT_OP.min_v, NOT_OP.max_v)
    dest.set_resistance(NOT_OP.preset_val)
    return execute(dest, src, None, None, None, None, v)

def BUFF(dest, src):
    v = src.get_voltage()
    check_voltage(v, BUFF_OP.min_v, BUFF_OP.max_v)
    dest.set_resistance(BUFF_OP.preset_val)
    return execute(dest, src, None, None, None, None, v)

def NAND(dest, src1, src2):
    v = src1.get_voltage()
    check_voltage(v, NAND_OP.min_v, NAND_OP.max_v)
    dest.set_resistance(NAND_OP.preset_val)
    return execute(dest, src1, src2, None, None, None, v) 

def NOR(dest, src1, src2):
    v = src1.get_voltage()
    check_voltage(v, NOR_OP.min_v, NOR_OP.max_v)
    dest.set_resistance(NOR_OP.preset_val)
    return execute(dest, src1, src2, None, None, None, v)

def MAJ3(dest, src1, src2, src3):
    v = src1.get_voltage()
    check_voltage(v, MAJ3_OP.min_v, MAJ3_OP.max_v)
    dest.set_resistance(MAJ3_OP.preset_val)
    return execute(dest, src1, src2, src3, None, None, v)

def MAJ5(dest, src1, src2, src3, src4, src5):
    v = src1.get_voltage()
    check_voltage(v, MAJ5_OP.min_v, MAJ5_OP.max_v)
    dest.set_resistance(MAJ5_OP.preset_val)
    return execute(dest, src1, src2, src3, src4, src5, v)

def NMAJ3(dest, src1, src2, src3):
    v = src1.get_voltage()
    check_voltage(v, NMAJ3_OP.min_v, NMAJ3_OP.max_v)
    dest.set_resistance(NMAJ3_OP.preset_val)
    return execute(dest, src1, src2, src3, None, None, v)

def NMAJ5(dest, src1, src2, src3, src4, src5):
    v = src1.get_voltage()
    check_voltage(v, NMAJ5_OP.min_v, NMAJ5_OP.max_v)
    dest.set_resistance(NMAJ5_OP.preset_val)
    return execute(dest, src1, src2, src3, src4, src5, v)

def WRITE(bits):
    return WRITE_TIME, WRITE_ENERGY*bits

def READ(bits):
    return READ_TIME, READ_ENERGY*bits

############### HELPER FUNCTIONS ###############

def check_voltage(voltage, min_v, max_v) -> None:
    if (voltage < min_v) or (voltage > max_v):
        raise ValueError("Applied voltage is not appropriate!")

def calculate_energy(curren, voltage):
    return (((curren * voltage * TWR) / 1000) + E_PRESET); #(fJ)

def calculate_current(dest_om, src1_om, src2_om, src3_om, src4_om, src5_om, voltage):
    result = 0
    if src2_om is None:
        result = (voltage / (src1_om + dest_om)); #(uA)
    elif src3_om is None:
        result = (voltage / (((src1_om * src2_om) / (src1_om + src2_om)) + dest_om)); #(uA)
    elif src4_om is None and src5_om is None:
        result = (voltage / (((src1_om * src2_om * src3_om) / (src1_om + src2_om + src3_om)) + dest_om)); #(uA)
    else:
        result = (voltage / (((src1_om * src2_om * src3_om * src4_om * src5_om) / (src1_om + src2_om + src3_om + src4_om + src5_om)) + dest_om)); #(uA)
    return result

def execute(dest, src1, src2, src3, src4, src5, voltage):
    dest_resistance = dest.get_resistance_om()
    src1_resistance = src1.get_resistance_om()
    src2_resistance = None if src2 is None else src2.get_resistance_om()
    src3_resistance = None if src3 is None else src3.get_resistance_om()
    src4_resistance = None if src4 is None else src4.get_resistance_om()
    src5_resistance = None if src5 is None else src5.get_resistance_om()
    current = calculate_current(dest_resistance, src1_resistance, src2_resistance, src3_resistance, src4_resistance, src5_resistance, voltage)
    energy = calculate_energy(current, voltage)
    if current > IC:
        if dest.get_resistance():
            dest.set_resistance(False)
        else:
            dest.set_resistance(True) #Toggle bit 

    time = TWR + ROW_DECODER_TIME + COLUMN_DECODER_TIME
    energy += ROW_DECODER_ENERGY + COLUMN_DECODER_ENERGY
    return time, energy

