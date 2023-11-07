#include <msp430.h>
#include <stdlib.h>
#include <stdint.h>
#include <nvs.h>
#include <ctpl.h>
#include <ctpl_low_level.h>

#include <fram.h>
#include <input.h>
#include <conv1.h>
#include <conv2.h>
#include <conv3.h>
#include <fc1.h>
#include <viadottolib/viadotto.h>

uint8_t tileID[32] = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
                        0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F,
                        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17,
                        0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F};

#define OUTPUT_LEN 1024
fixed output1[OUTPUT_LEN];
fixed output2[OUTPUT_LEN];


void initClockTo16MHz(void);
void initGPIO(void);
void initUART(void);

/**
 * main.c
 */
int main(void)
{
    WDTCTL = WDTPW | WDTHOLD;   // stop watchdog timer
    PM5CTL0 &= ~LOCKLPM5; // Disable the GPIO power-on default high-impedance mode

    initClockTo16MHz();
    initGPIO();
    initUART();

    data.i = 0;
    data.j = 0;
    data.k = 0;
    data.m = 0;
    data.n = 0;

    nvsHandle = nvs_data_init(nvsStorage1, sizeof(data_t));
    status = nvs_data_restore(nvsHandle, &data);
    ctpl_init();

    //We assume that input data and kernels are already aligned as required by CRAM


    for(; data.i < 32; data.i++){
        cram_tile_enable(tileID[data.i]);
        cram_load_ina(tileID[data.i], input, INPUT_LEN);
        cram_load_inb(tileID[data.i], conv1, CONV1_LEN);
        cram_bias_enable(CONV1_BIAS_LEN);
    }

    cram_mac();
    cram_move_out_in();

    for(; data.j < 32; data.j++){
        cram_tile_enable(tileID[data.j]);
        cram_load_inb(tileID[data.j], conv2, CONV2_LEN);
        cram_bias_enable(CONV2_BIAS_LEN);
    }

    cram_mac();
    cram_move_out_in();
    cram_relu();
    cram_move_out_in();
    cram_maxpool();
    cram_move_out_in();

    for(; data.k < 32; data.k++){
        cram_tile_enable(tileID[data.k]);
        cram_load_inb(tileID[data.k], conv3, CONV3_LEN);
        cram_bias_enable(CONV3_BIAS_LEN);
    }

    cram_mac();
    cram_move_out_in();
    cram_relu();
    cram_move_out_in();
    cram_maxpool();
    cram_move_out_in();

    for(; data.m < 32; data.m++){
        cram_tile_enable(tileID[data.m]);
        cram_load_inb(tileID[data.m], fc1, FC1_LEN);
        cram_bias_enable(FC1_BIAS_LEN);
    }

    cram_mult();
    cram_move_out_in();
    cram_add();

    //Only two unloads just as an example
    cram_unload_out(tileID[0], output1, OUTPUT_LEN);
    cram_unload_out(tileID[1], output2, OUTPUT_LEN);

    for(; data.n < 32; data.n++){
        cram_tile_disable(tileID[data.n]);
    }

    return 0;
}


void initClockTo16MHz(void){
    // Configure one FRAM waitstate as required by the device datasheet for MCLK
    // operation beyond 8MHz _before_ configuring the clock system.
    FRCTL0 = FRCTLPW | NWAITS_1;

    // Clock System Setup
    CSCTL0_H = CSKEY_H;                     // Unlock CS registers
    CSCTL1 = DCOFSEL_0;                     // Set DCO to 1MHz

    // Set SMCLK = MCLK = DCO, ACLK = VLOCLK
    CSCTL2 = SELA__VLOCLK | SELS__DCOCLK | SELM__DCOCLK;

    // Per Device Errata set divider to 4 before changing frequency to
    // prevent out of spec operation from overshoot transient
    CSCTL3 = DIVA__4 | DIVS__4 | DIVM__4;   // Set all corresponding clk sources to divide by 4 for errata
    CSCTL1 = DCOFSEL_4 | DCORSEL;           // Set DCO to 16MHz

    // Delay by ~10us to let DCO settle. 60 cycles = 20 cycles buffer + (10us / (1/4MHz))
    __delay_cycles(60);
    CSCTL3 = DIVA__1 | DIVS__1 | DIVM__1;   // Set all dividers to 1 for 16MHz operation
    CSCTL0_H = 0;                           // Lock CS registers
}

void initGPIO(void){
    // Configure GPIO
    P6OUT = 0x0; //Clear OUTPUT of P6
    P6DIR = 0xFF;
    //SPI master for the external FRAM
    P6SEL1 &= ~(BIT0 | BIT1 | BIT2 | BIT3); // USCI_A3 SCLK, MOSI, and MISO pin
    P6SEL0 |= (BIT0 | BIT1 | BIT2 | BIT3);

    // Disable the GPIO power-on default high-impedance mode to activate
    // previously configured port settings
    PM5CTL0 &= ~LOCKLPM5;
}

void initUART(void)
{    //Status pins
    P4OUT &= ~BIT1;                     //Clear OUTPUT of P4.1
    P4OUT &= ~BIT2;                     //Clear OUTPUT of P4.2
    //MC enable bit
    P4OUT &= ~BIT3;                     //Clear OUTPUT of P4.3
    P4DIR |= BIT3;                      //Define OUT direction of P4.3


    P2SEL1 |= BIT5 + BIT6;              //Activate Pin for UART use
    P2SEL0 &= ~BIT5 + ~BIT6;            //Activate Pin for UART use

    UCA1CTLW0 = UCSWRST;                // Put eUSCI in reset
    UCA1CTLW0 |= UCSSEL__SMCLK;         // CLK = SMCLK

    UCA1BRW = 0x6;                      //Set Baud rate 9600 : UCA1BRW = INT(F_CPU/BAUD_soll) =         INT(1MHz/9600) = 104 with oversampling: 6
    UCA1MCTLW |= UCBRS5 + UCOS16 + UCBRF3;     //Modulation according to datasheet table: UCBRS = 0x20 = b100000 and UCOS16 = 1 and UCBRF = 8 = 0x8 = b1000

    UCA1CTLW0 &= ~UCSWRST;              //Reset UART modulet
}



