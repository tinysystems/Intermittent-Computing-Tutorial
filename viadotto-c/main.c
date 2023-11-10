
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include "input.h"
#include "conv1.h"
#include "conv2.h"
#include "conv3.h"
#include "fc1.h"
#include "viadotto.h"

#define MNIST
//#define ESC

uint8_t tileID[32] = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 
                        0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 
                        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 
                        0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F};

#define OUTPUT_LEN 10
fixed output[OUTPUT_LEN];

FILE *fpt;
uint8_t active_tiles = 32;
uint16_t inputs = 32;
char file_name[30];


/**
 * main.c
 */
int main(void)
{
    
    int i = 0;
    int j = 0;
    int k = 0;
    int m = 0;
    int n = 0;
    int p = 0;
    char cnnmodel[10];
#ifdef MNIST
    sprintf(cnnmodel, "mnist");
#endif
#ifdef ESC
    sprintf(cnnmodel, "esc");
#endif
    sprintf(file_name, "../CRAM/mcu_to_mc_%d_%s.csv", active_tiles, cnnmodel);
    fpt = fopen(file_name, "w+");
    //fprintf(fpt, "OPCODE tileID size\n");
    
    // Specify the number of tiles you want to activate and how many inputs you will have in total.
    // Make sure to meet the following condition: inputs % active_tiles == 0
    fprintf(fpt, "%d %d\n", active_tiles, inputs);

    //We assume that input data and kernels are already aligned as required by CRAM

#ifdef MNIST
    for(; i < active_tiles; i++){
        cram_tile_enable(tileID[i], fpt);
        cram_load_ina(tileID[i], input, INPUT_LEN, fpt);
        cram_load_inb(tileID[i], conv1, CONV1_LEN, fpt);
        cram_bias_enable(CONV1_BIAS_LEN, fpt);
    }

    cram_mac(fpt);
    cram_move_out_in(fpt);

    for(; j < active_tiles; j++){
        cram_load_inb(tileID[j], conv2, CONV2_LEN, fpt);
        cram_bias_enable(CONV2_BIAS_LEN, fpt);
    }

    cram_mac(fpt);
    cram_move_out_in(fpt);
    cram_relu(fpt);
    cram_move_out_in(fpt);
    cram_maxpool(fpt);
    cram_move_out_in(fpt);

    for(; k < active_tiles; k++){
        cram_load_inb(tileID[k], conv3, CONV3_LEN, fpt);
        cram_bias_enable(CONV3_BIAS_LEN, fpt);
    }

    cram_mac(fpt);
    cram_move_out_in(fpt);
    cram_relu(fpt);
    cram_move_out_in(fpt);
    cram_maxpool(fpt);
    cram_move_out_in(fpt);

    for(; m < active_tiles; m++){
        cram_load_inb(tileID[m], fc1, FC1_LEN, fpt);
        cram_bias_enable(FC1_BIAS_LEN, fpt);
    }

    cram_mult(fpt);
    cram_move_out_in(fpt);
    cram_add(fpt);

    for(; n < active_tiles; n++){
        cram_unload_out(tileID[n], output, OUTPUT_LEN, fpt);
    }
    
    for(; p < active_tiles; p++){
        cram_tile_disable(tileID[p], fpt);
    }
#endif
#ifdef ESC
    for(; i < active_tiles; i++){
        cram_tile_enable(tileID[i], fpt);
        cram_load_ina(tileID[i], input, INPUT_LEN, fpt);
        cram_load_inb(tileID[i], conv1, CONV1_LEN, fpt);
        cram_bias_enable(CONV1_BIAS_LEN, fpt);
    }

    cram_mac(fpt);
    cram_move_out_in(fpt);

    for(; j < active_tiles; j++){
        cram_load_inb(tileID[j], conv2, CONV2_LEN, fpt);
        cram_bias_enable(CONV2_BIAS_LEN, fpt);
    }

    cram_mac(fpt);
    cram_move_out_in(fpt);
    cram_relu(fpt);
    cram_move_out_in(fpt);
    cram_maxpool(fpt);
    cram_move_out_in(fpt);

    for(; k < active_tiles; k++){
        cram_load_inb(tileID[k], fc1, FC1_LEN, fpt);
        cram_bias_enable(FC1_BIAS_LEN, fpt);
    }

    cram_mac(fpt);
    cram_move_out_in(fpt);
    cram_relu(fpt);
    cram_move_out_in(fpt);
    cram_maxpool(fpt);
    cram_move_out_in(fpt);

    for(; m < active_tiles; m++){
        cram_load_inb(tileID[m], fc1, FC1_LEN, fpt);
        cram_bias_enable(FC1_BIAS_LEN, fpt);
    }

    cram_mult(fpt);
    cram_move_out_in(fpt);
    cram_add(fpt);

    for(; n < active_tiles; n++){
        cram_unload_out(tileID[n], output, OUTPUT_LEN, fpt);
    }
    
    for(; p < active_tiles; p++){
        cram_tile_disable(tileID[p], fpt);
    }
#endif

    fclose(fpt);
    return 0;
}


