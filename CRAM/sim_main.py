from csv import reader
import random
import numpy as np

from array import *
from params import *
from MC import *
from logic import AND, OR, NOT, BUFF, NAND, NOR, MAJ3, MAJ5, NMAJ3, NMAJ5
import MTJ as mtj


def generate_powtrace(file):
    data = np.loadtxt(file)[:, 1] # Data in uW
    return data

def create_tile(height, width):
    tile = [] #tile of MTJs
    for i in range(height):
        tile.append([])
        for j in range(width):
            tile[i].append(mtj.MTJ(False, 0))
    return tile

def select_mode(p):
    mode = '1'
    for key, value in power_dic.items():
        if p >= value:
            mode = key
            break
    
    return mode



def main():
    # height = 1024
    # width = 1024
    # tiles = 32
    # cram_grid = []
    # for i in range(tiles):
    #     cram_grid.append(create_tile(height, width))

    iterations = 0
    processed_images = 0
    finish = 0
    powtr = generate_powtrace(CAR)
    print(powtr)
    poweriterator = 0
    while not finish:
        if poweriterator == len(powtr):
            poweriterator = 0
        update_pamb(1000000000000)#(powtr[poweriterator])
        poweriterator += 1

        cnnmodel = "mnist"
        mode = '1' #select_mode(p)
        filename = 'mcu_to_mc_' + mode + '_' + cnnmodel + '.csv'
        with open(filename, 'r') as f:
            tiles, inputs = (f.readline()).split()
            tiles, inputs = int(tiles), int(inputs)
            if tiles > AVAILABLE_TILES:
                raise ValueError("Activated tiles exceed the number of tiles available in CRAM!")
            else:
                if inputs % tiles != 0:
                    raise ValueError("Make sure to meet the following condition: inputs % active_tiles == 0!")
                else:
                    iterations = inputs//tiles
        
        
        while iterations:
            instruction = 1
            
            with open(filename, 'r') as read_obj:
                next(read_obj)
                # pass the file object to reader() to get the reader object
                csv_reader = reader(read_obj)
                # Iterate over each row in the csv using reader object
                for row in csv_reader:
                    if time_elapsed():
                        finish = 1
                        break
                    # row variable is a list that represents a row in csv
                    opcode, tileid, size = row[0].split()
                    opcode, tileid, size = int(opcode), int(tileid), int(size)
                    process_HL_instruction(opcode, tileid, size, instruction)
                    instruction += 1
            
            iterations -= 1
        
        if not finish:
            processed_images += int(mode)

    print_result()
    print("Processed images - ", processed_images)
            



if __name__ == "__main__":
    main()