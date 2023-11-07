from pathlib import Path

########## CRAM paremeters ##########

AVAILABLE_TILES = 32
RAP = 7.34 #76.39; #Antiparallel resistance (KOhm)
RP = 3.15 #12.73; #Parallel resistance (KOhm)
IC = 50 #0.79; #Switching current (uA)
TWR = 3; #Switching time (ns)
E_PRESET = 66 #26.1; #P = 50 uA * 433 mV = 22 uW; E_PRESET = 22 uW * 3 ns = 66 fJ (433 mV is average voltage for NOT gate)
# From NVsim: 128KB STTRAM_cache, ReadEDP optimization
WRITE_ENERGY = 542254 # (fJ)
READ_ENERGY = 123724 # (fJ)
WRITE_TIME = 10.5 # (ns)
READ_TIME = 2 # (ns)
LEAKAGE_POWER = 31 # (mW)
ROW_DECODER_ENERGY = 58 # (fJ)
COLUMN_DECODER_ENERGY = 58 # (fJ)
ROW_DECODER_TIME = 0.2 # (ns)
COLUMN_DECODER_TIME = 0.2 # (ns)


class OP:
    min_v = 0.0
    max_v = 0.0
    preset_val = False

#I = V / [(R1*R2/(R1 + R2)) + R0] - the main formula

#V00 < V01 = V10 < Vand < V11
AND_OP = OP()
AND_OP.min_v = IC * (((RAP * RP) / (RAP + RP)) + RAP) #V10
AND_OP.max_v = IC * (((RAP * RAP) / (RAP + RAP)) + RAP) #V11
AND_OP.preset_val = True

#V00 < Vor < V01 = V10 < V11
OR_OP = OP()
OR_OP.min_v = IC * (((RP * RP) / (RP + RP)) + RAP) #V00
OR_OP.max_v = IC * (((RP * RAP) / (RP + RAP)) + RAP) #V01
OR_OP.preset_val = True

#V0 < Vnot < V1
NOT_OP = OP()
NOT_OP.min_v = IC * (RP + RP) #V0
NOT_OP.max_v = IC * (RAP + RP) #V1
NOT_OP.preset_val = False

#V0 < Vbuff < V1
BUFF_OP = OP()
BUFF_OP.min_v = IC * (RP + RAP) #V0
BUFF_OP.max_v = IC * (RAP + RAP) #V1
BUFF_OP.preset_val = True

#V00 < V01 = V10 < Vnand < V11
NAND_OP = OP()
NAND_OP.min_v = IC * (((RAP * RP) / (RAP + RP)) + RP) #V10
NAND_OP.max_v = IC * (((RAP * RAP) / (RAP + RAP)) + RP) #V11
NAND_OP.preset_val = False

#V00 < Vor < V01 = V10 < V11
NOR_OP = OP()
NOR_OP.min_v = IC * (((RP * RP) / (RP + RP)) + RP) #V00
NOR_OP.max_v = IC * (((RP * RAP) / (RP + RAP)) + RP) #V01
NOR_OP.preset_val = False

#V000 < V001 = V010 = V100 < Vmaj3 < V011 = V101 = V110 < V111
MAJ3_OP = OP()
MAJ3_OP.min_v = IC * (((RAP * RP * RP) / (RAP + RP + RP)) + RAP) #V100
MAJ3_OP.max_v = IC * (((RP * RAP * RAP) / (RP + RAP + RAP)) + RAP) #V011
MAJ3_OP.preset_val = True

#V00000 < ... = V11000 < Vmaj5 < V00111 = ... < V11111
MAJ5_OP = OP()
MAJ5_OP.min_v = IC * (((RAP * RAP * RP * RP * RP) / (RAP + RAP + RP + RP + RP)) + RAP) #V11000
MAJ5_OP.max_v = IC * (((RP * RP * RAP * RAP * RAP) / (RP + RP + RAP + RAP + RAP)) + RAP) #V00111
MAJ5_OP.preset_val = True

#V000 < V001 = V010 = V100 < Vmaj3 < V011 = V101 = V110 < V111
NMAJ3_OP = OP()
NMAJ3_OP.min_v = IC * (((RAP * RP * RP) / (RAP + RP + RP)) + RP) #V100
NMAJ3_OP.max_v = IC * (((RP * RAP * RAP) / (RP + RAP + RAP)) + RP) #V011
NMAJ3_OP.preset_val = False

#V00000 < ... = V11000 < Vmaj5 < V00111 = ... < V11111
NMAJ5_OP = OP()
NMAJ5_OP.min_v = IC * (((RAP * RAP * RP * RP * RP) / (RAP + RAP + RP + RP + RP)) + RP) #V11000
NMAJ5_OP.max_v = IC * (((RP * RP * RAP * RAP * RAP) / (RP + RP + RAP + RAP + RAP)) + RP) #V00111
NMAJ5_OP.preset_val = False


########## MC paremeters ##########
MOUSE = 1

# At 100 MHz
MC_READ_TIME = 10 # (ns)
MC_WRITE_TIME = 10 # (ns)
MC_DECODE_TIME = 10 # (ns)
MC_EXECUTE_TIME = 10 # (ns)

if MOUSE:
    # At 30 MHz
    MC_READ_TIME = 33 # (ns)
    MC_WRITE_TIME = 33 # (ns)
    MC_DECODE_TIME = 33 # (ns)
    MC_EXECUTE_TIME = 33 # (ns)

# At 0.46 mW
MC_READ_ENERGY = 4600 # (fJ)
MC_WRITE_ENERGY = 4600 # (fJ)
MC_DECODE_ENERGY = 4600 # (fJ)
MC_EXECUTE_ENERGY = 4600 # (fJ)

OPCODE_enable =       0x01
OPCODE_disable =      0x02
OPCODE_ina =          0x03
OPCODE_inb =          0x04
OPCODE_bias_enable =  0x05
OPCODE_unload =       0x06
OPCODE_move =         0x07
OPCODE_add =          0x08
OPCODE_mult =         0x09
OPCODE_relu =         0x0A
OPCODE_maxpool =      0x0B
OPCODE_mac =          0x0C

WORD_width = 8 # bits
IN_width = 512 # bits
CA_width = 9 # words
MAXPOOL_vector = 4 # 2x2
# Сounted manually
BUFFS_in_ADD = 1
NANDS_in_ADD = 10 
BUFFS_in_MULT = 8
NANDS_in_MULT = NANDS_in_ADD * 3
BUFFS_in_RELU = 1
NANDS_in_RELU = 1
NOTS_in_MAXPOOL = 1
ANDS_in_MAXPOOL = 4
ORS_in_MAXPOOL = 2
BUFFS_in_MAC = BUFFS_in_MULT + BUFFS_in_ADD # * CA_width ??? Check if we need these
NANDS_in_MAC =  NANDS_in_MULT + NANDS_in_ADD # * CA_width ???


########## APP parameters ##########
C = 0.6 # (mF)
CAP_ENERGY = (((3.3**2 - 1.8**2)*C)/2)*1000000000000 # (fJ)

CRAM_ONLY = 0
ADAPTIVE = 1

MNIST = 0
ESC = 1
CNN_TYPE = MNIST

MNIST_INPUT = 784
MNIST_CONV1_MAC = 7840
MNIST_CONV1_RELU = 7840
MNIST_CONV2_MAC = 11520
MNIST_CONV2_RELU = 11520
MNIST_CONV2_MAXPOOL = 2880
MNIST_CONV3_MAC = 3200
MNIST_CONV3_RELU = 3200
MNIST_CONV3_MAXPOOL = 1600
MNIST_FC1_MULT = 800000
MNIST_FC1_ADD = 800000
MNIST_FC1_RELU = 500
MNIST_FC2_MULT = 5000
MNIST_FC2_ADD = 5000
MNIST_FC2_RELU = 10

ESC_INPUT = 3072
ESC_CONV1_MAC = 39200
ESC_CONV1_RELU = 39200
ESC_CONV1_MAXPOOL = 9800
ESC_CONV2_MAC = 10000
ESC_CONV2_RELU = 10000
ESC_CONV2_MAXPOOL = 2500
ESC_FC1_MULT = 250000
ESC_FC1_ADD = 250000
ESC_FC1_RELU = 100
ESC_FC2_MULT = 250000
ESC_FC2_ADD = 250000
ESC_FC2_RELU = 100

if CNN_TYPE == MNIST:
    MAC_LAYERS = [0, MNIST_CONV1_MAC, MNIST_CONV2_MAC, MNIST_CONV3_MAC, 0, 0]
    RELU_LAYERS = [0, MNIST_CONV1_RELU, MNIST_CONV2_RELU, MNIST_CONV3_RELU, MNIST_FC1_RELU, MNIST_FC2_RELU]
    MAXPOOL_LAYERS = [0, 0, MNIST_CONV2_MAXPOOL, MNIST_CONV3_MAXPOOL, 0, 0]
    MULT_LAYERS = [0, 0, 0, 0, MNIST_FC1_MULT, MNIST_FC2_MULT]
    ADD_LAYERS = [0, 0, 0, 0, MNIST_FC1_ADD, MNIST_FC2_ADD]
else:
    MAC_LAYERS = [0, ESC_CONV1_MAC, ESC_CONV2_MAC, 0, 0]
    RELU_LAYERS = [0, ESC_CONV1_RELU, ESC_CONV2_RELU, ESC_FC1_RELU, ESC_FC2_RELU]
    MAXPOOL_LAYERS = [0, ESC_CONV1_MAXPOOL, ESC_CONV2_MAXPOOL, 0, 0]
    MULT_LAYERS = [0, 0, 0, ESC_FC1_MULT, ESC_FC2_MULT]
    ADD_LAYERS = [0, 0, 0, ESC_FC1_ADD, ESC_FC2_ADD]

APP_TIME = 100000000000 #(ns) 10 s

NIGHT = Path('../power-traces/mobile-nyt-nighttime.txt')
CAR = Path('../power-traces/mobile-car.txt')
MIX = Path('../power-traces/mobile-indoor-outdoor.txt')

########## MCU parameters ##########

MCU_POWER = 10000 #(uW)
if MOUSE:
    MCU_POWER = 5000


########## POWER parameters ##########

power_dic = {
    '32': 100,
    '16': 100,
    '8': 100,
    '4': 100,
    '2': 100,
    '1': 100
}