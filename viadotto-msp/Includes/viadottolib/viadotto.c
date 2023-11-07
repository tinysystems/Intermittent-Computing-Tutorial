#include <stdlib.h>
#include <extfram.h>
#include <Includes/viadottolib/viadotto.h>

EXTFRAM_ADDR baseAddress = {0x00, 0x00, 0x00};

void cram_tile_enable(uint8_t tileID){

    wait_idle();
    UCA1TXBUF = OPCODE_enable;
    CHECKPOINT();
    wait_idle();
    UCA1TXBUF = tileID;
    CHECKPOINT();
    enable_MC();
    CHECKPOINT();
    wait_finished();

    return;
}

void cram_tile_disable(uint8_t tileID){

    wait_idle();
    UCA1TXBUF = OPCODE_disable;
    CHECKPOINT();
    wait_idle();
    UCA1TXBUF = tileID;
    CHECKPOINT();
    enable_MC();
    CHECKPOINT();
    wait_finished();

    return;
}

void cram_load_ina(uint8_t tileID, fixed* input, uint16_t size){

    fixed* ptr = input;
    uint16_t counter = size;
    while(counter < size){
        if(ptr != NULL){
            UCA1TXBUF = *ptr;
            ptr++;
            counter--;
        }
    }
    CHECKPOINT();
    wait_idle();
    UCA1TXBUF = OPCODE_ina;
    CHECKPOINT();
    enable_MC();
    CHECKPOINT();
    wait_finished();

    return;
}

void cram_load_inb(uint8_t tileID, fixed* input, uint16_t size){

    fixed* ptr = input;
    uint16_t counter = size;
    while(counter > 0){
        wait_idle();
        if(ptr != NULL){
            UCA1TXBUF = *ptr;
            ptr++;
            counter--;
        }
    }
    CHECKPOINT();
    wait_idle();
    UCA1TXBUF = OPCODE_inb;
    CHECKPOINT();
    enable_MC();
    CHECKPOINT();
    wait_finished();

    return;
}

void cram_bias_enable(uint16_t size){

    wait_idle();
    UCA1TXBUF = OPCODE_bias_enable;
    CHECKPOINT();
    wait_idle();
    UCA1TXBUF = size;
    CHECKPOINT();
    enable_MC();
    CHECKPOINT();
    wait_finished();

    return;
}

void cram_unload_out(uint8_t tileID, fixed* output, uint16_t size){

    fixed* ptr = output;
    uint16_t counter = size;

    wait_idle();
    UCA1TXBUF = OPCODE_unload;
    CHECKPOINT();
    enable_MC();
    CHECKPOINT();
    wait_finished();

    while(counter > 0){
        while(!(UCA1IFG & UCRXIFG));
        if(ptr != NULL){
            *ptr = UCA1RXBUF;
            ptr++;
            counter--;
        }
    }
    CHECKPOINT();

    return;
}

void cram_move_out_in(){

    wait_idle();
    UCA1TXBUF = OPCODE_move;
    CHECKPOINT();
    enable_MC();
    CHECKPOINT();
    wait_finished();

    return;
}

void cram_add(){

    wait_idle();
    UCA1TXBUF = OPCODE_add;
    CHECKPOINT();
    enable_MC();
    CHECKPOINT();
    wait_finished();
    return;
}

void cram_mult(){

    wait_idle();
    UCA1TXBUF = OPCODE_mult;
    CHECKPOINT();
    enable_MC();
    CHECKPOINT();
    wait_finished();
    return;
}

void cram_relu(){

    wait_idle();
    UCA1TXBUF = OPCODE_relu;
    CHECKPOINT();
    enable_MC();
    CHECKPOINT();
    wait_finished();
    return;
}

void cram_maxpool(){

    wait_idle();
    UCA1TXBUF = OPCODE_maxpool;
    CHECKPOINT();
    enable_MC();
    CHECKPOINT();
    wait_finished();
    return;
}

void cram_mac(){

    wait_idle();
    UCA1TXBUF = OPCODE_mac;
    CHECKPOINT();
    enable_MC();
    CHECKPOINT();
    wait_finished();
    return;
}

void wait_idle(){

    while(!(UCA1IFG & UCTXIFG));
    uint8_t status = 0xFF;
    while(status != IDLE)
        readEXTFRAM(baseAddress, &status, 1);
}

void wait_finished(){

    uint8_t status = 0xFF;
    while(status != FINISHED)
        readEXTFRAM(baseAddress, &status, 1);

    writeEXTFRAM(baseAddress, IDLE, 1);
}

void enable_MC(){
    uint8_t status = 0xFF;
    readEXTFRAM(baseAddress, &status, 1);
    CHECKPOINT();
    if(status == IDLE)
        P4OUT |= BIT3;
}

void CHECKPOINT(){

    status = nvs_data_commit(nvsHandle, &data);
    ctpl_saveCpuStackEnterLpm(CTPL_MODE_NONE,0);
}
