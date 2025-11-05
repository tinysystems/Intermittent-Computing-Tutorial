#include <stdlib.h>
#include <stdio.h>
#include "viadotto.h"

void cram_tile_enable(uint8_t tileID, FILE *fpt){

    fprintf(fpt,"%d %d %d\n", OPCODE_enable, tileID, 0); 
    
    // wait_idle();
    // UCA1TXBUF = OPCODE_enable;
    // CHECKPOINT();
    // wait_idle();
    // UCA1TXBUF = tileID;
    // CHECKPOINT();
    // enable_MC();
    // CHECKPOINT();
    // wait_finished();
    return;
}

void cram_tile_disable(uint8_t tileID, FILE *fpt){

    fprintf(fpt,"%d %d %d\n", OPCODE_disable, tileID, 0); 
    // wait_idle();
    // UCA1TXBUF = OPCODE_disable;
    // CHECKPOINT();
    // wait_idle();
    // UCA1TXBUF = tileID;
    // CHECKPOINT();
    // enable_MC();
    // CHECKPOINT();
    // wait_finished();
    return;
}

void cram_load_ina(uint8_t tileID, fixed* input, uint16_t size, FILE *fpt){

    // fprintf(fpt,"%d %d %d\n", OPCODE_ina, tileID, size); //For training presentation only 
	
    uint16_t counter = size;
    while(counter > 0){
        fprintf(fpt,"%d %d %d\n", OPCODE_ina, tileID, size);
        counter--;
    }	
	
    // fixed* ptr = input;
    // uint16_t counter = size;
    // while(counter > 0){
	//	   wait_idle();
    //     if(ptr != NULL){
    //         UCA1TXBUF = *ptr;
    //         ptr++;
    //         counter--;
    //     }
    // }
    // CHECKPOINT();
    // wait_idle();
    // UCA1TXBUF = OPCODE_ina;
    // CHECKPOINT();
    // enable_MC();
    // CHECKPOINT();
    // wait_finished();

    return;
}

void cram_load_inb(uint8_t tileID, fixed* input, uint16_t size, FILE *fpt){

    // fprintf(fpt,"%d %d %d\n", OPCODE_inb, tileID, size); //For training presentation only
    
	uint16_t counter = size;
    while(counter > 0){
        fprintf(fpt,"%d %d %d\n", OPCODE_inb, tileID, size);
        counter--;
    }
	
    // fixed* ptr = input;
    // uint16_t counter = size;
    // while(counter > 0){
    //     wait_idle();
    //     if(ptr != NULL){
    //         UCA1TXBUF = *ptr;
    //         ptr++;
    //         counter--;
    //     }
    // }
    // CHECKPOINT();
    // wait_idle();
    // UCA1TXBUF = OPCODE_inb;
    // CHECKPOINT();
    // enable_MC();
    // CHECKPOINT();
    // wait_finished();

    return;
}

void cram_bias_enable(uint16_t size, FILE *fpt){

    fprintf(fpt,"%d %d %d\n", OPCODE_bias_enable, 0, size);

    // wait_idle();
    // UCA1TXBUF = OPCODE_bias_enable;
    // CHECKPOINT();
    // wait_idle();
    // UCA1TXBUF = size;
    // CHECKPOINT();
    // enable_MC();
    // CHECKPOINT();
    // wait_finished();

    return;
}

void cram_unload_out(uint8_t tileID, fixed* output, uint16_t size, FILE *fpt){

    // fprintf(fpt,"%d %d %d\n", OPCODE_unload, tileID, size); //For training presentation only
	
	uint16_t counter = size;
    while(counter > 0){
        fprintf(fpt,"%d %d %d\n", OPCODE_unload, tileID, size);
        counter--;
    }
	
    // fixed* ptr = output;
    // uint16_t counter = size;

    // wait_idle();
    // UCA1TXBUF = OPCODE_unload;
    // CHECKPOINT();
    // enable_MC();
    // CHECKPOINT();
    // wait_finished();

    // while(counter > 0){
    //     while(!(UCA1IFG & UCRXIFG));
    //     if(ptr != NULL){
    //         *ptr = UCA1RXBUF;
    //         ptr++;
    //         counter--;
    //     }
    // }
    // CHECKPOINT();

    return;
}

void cram_move_out_in(FILE *fpt){

    fprintf(fpt,"%d %d %d\n", OPCODE_move, 0, 0);

    // wait_idle();
    // UCA1TXBUF = OPCODE_move;
    // CHECKPOINT();
    // enable_MC();
    // CHECKPOINT();
    // wait_finished();

    return;
}

void cram_add(FILE *fpt){

    fprintf(fpt,"%d %d %d\n", OPCODE_add, 0, 0);

    // wait_idle();
    // UCA1TXBUF = OPCODE_add;
    // CHECKPOINT();
    // enable_MC();
    // CHECKPOINT();
    // wait_finished();
    return;
}

void cram_mult(FILE *fpt){

    fprintf(fpt,"%d %d %d\n", OPCODE_mult, 0, 0);

    // wait_idle();
    // UCA1TXBUF = OPCODE_mult;
    // CHECKPOINT();
    // enable_MC();
    // CHECKPOINT();
    // wait_finished();
    return;
}

void cram_relu(FILE *fpt){

    fprintf(fpt,"%d %d %d\n", OPCODE_relu, 0, 0);

    // wait_idle();
    // UCA1TXBUF = OPCODE_relu;
    // CHECKPOINT();
    // enable_MC();
    // CHECKPOINT();
    // wait_finished();
    return;
}

void cram_maxpool(FILE *fpt){

    fprintf(fpt,"%d %d %d\n", OPCODE_maxpool, 0, 0);

    // wait_idle();
    // UCA1TXBUF = OPCODE_maxpool;
    // CHECKPOINT();
    // enable_MC();
    // CHECKPOINT();
    // wait_finished();
    return;
}

void cram_mac(FILE *fpt){

    fprintf(fpt,"%d %d %d\n", OPCODE_mac, 0, 0);

    // wait_idle();
    // UCA1TXBUF = OPCODE_mac;
    // CHECKPOINT();
    // enable_MC();
    // CHECKPOINT();
    // wait_finished();
    return;
}

void wait_idle(){

    // while(!(UCA1IFG & UCTXIFG));
    // uint8_t status = 0xFF;
    // while(status != IDLE)
    //     readEXTFRAM(baseAddress, &status, 1);
}

void wait_finished(){

    // uint8_t status = 0xFF;
    // while(status != FINISHED)
    //     readEXTFRAM(baseAddress, &status, 1);

    // writeEXTFRAM(baseAddress, IDLE, 1);
}

void enable_MC(){
    // uint8_t status = 0xFF;
    // readEXTFRAM(baseAddress, &status, 1);
    // CHECKPOINT();
    // if(status == IDLE)
    //     P4OUT |= BIT3;
}


