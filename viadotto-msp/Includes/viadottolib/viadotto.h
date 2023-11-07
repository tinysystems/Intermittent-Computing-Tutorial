#ifndef VIADOTTO_H_
#define VIADOTTO_H_

#include <msp430.h>
#include <stdarg.h>
#include <stdint.h>
#include <includes/fixedlib/fixed.h>

#include <fram-utilities/nvs/nvs.h>
#include <ctpl.h>
#include <ctpl_low_level.h>

//FRAM utility stuff
typedef struct{
    uint16_t i;
    uint16_t j;
    uint16_t k;
    uint16_t m;
    uint16_t n;
} data_t;

data_t data;
uint8_t nvsStorage1[NVS_DATA_STORAGE_SIZE(sizeof(data_t))];
nvs_data_handle nvsHandle;
uint16_t status;


#define OPCODE_enable       0x01
#define OPCODE_disable      0x02
#define OPCODE_ina          0x03
#define OPCODE_inb          0x04
#define OPCODE_bias_enable  0x05
#define OPCODE_unload       0x06
#define OPCODE_move         0x07
#define OPCODE_add          0x08
#define OPCODE_mult         0x09
#define OPCODE_relu         0x0A
#define OPCODE_maxpool      0x0B
#define OPCODE_mac          0x0C

#define IDLE        0x00
#define BUSY        0x01
#define FINISHED    0x10



/* Function: cram_tile_enable
 * -----------------
 * sends tile ID to CRAM via UART and waits for the completion of
 * the specified tile to be enabled
 *
 * uint8_t: tile ID on CRAM
 *
 * returns: void
 */
void cram_tile_enable(uint8_t);

/* Function: cram_tile_disable
 * -----------------
 * sends tile ID to CRAM via UART and waits for the completion of
 * the specified tile to be disabled
 *
 * uint8_t: tile ID on CRAM
 *
 * returns: void
 */
void cram_tile_disable(uint8_t);

/* Function: cram_load_ina
 * -----------------
 * loads input data to the IN section of the specified tile
 *
 * uint8_t: tile ID on CRAM
 * uint8_t*: pointer to input data on MCU
 * uint16_t: input data size (bytes)
 *
 * returns: void
 */
void cram_load_ina(uint8_t, fixed*, uint16_t);

/* Function: cram_load_inb
 * -----------------
 * loads input data to the SD section of the specified tile
 *
 * uint8_t: tile ID on CRAM
 * uint8_t*: pointer to kernel data on MCU
 * uint16_t: input data size (bytes)
 *
 * returns: void
 */
void cram_load_inb(uint8_t, fixed*, uint16_t);

/* Function: cram_bias_enable
 * -----------------
 * extracts the biases from the loaded kernel.
 * You need to put biases to the very end of the kernel array
 *
 * uint16_t: bias data size (bytes)
 *
 * returns: void
 */
void cram_bias_enable(uint16_t);

/* Function: cram_unload_out
 * -----------------
 * unloads data from the OUT section of the specified tile
 *
 * uint8_t: tile ID on CRAM
 * uint8_t*: memory pointer where to put CRAM result on MCU
 * uint16_t: output data size (bytes)
 *
 * returns: void
 */
void cram_unload_out(uint8_t, fixed*, uint16_t);

/* Function: cram_move_out_in
 * -----------------
 * moves data from OUT section to IN section on CRAM
 * on all active tiles
 *
 * uint8_t: the number of cores to activate
 *
 * returns: void
 */
void cram_move_out_in();

/* Function: cram_add
 * -----------------
 * enables ADD operation on CRAM on all active tiles
 *
 *
 * returns: void
 */
void cram_add();

/* Function: cram_mult
 * -----------------
 * enables MULT operation on CRAM on all active tiles
 *
 *
 * returns: void
 */
void cram_mult();

/* Function: cram_relu
 * -----------------
 * enables RELU operation on CRAM on all active tiles
 *
 *
 * returns: void
 */
void cram_relu();

/* Function: cram_maxpool
 * -----------------
 * enables MAXPOOL operation on CRAM on all active tiles
 *
 *
 * returns: void
 */
void cram_maxpool();

/* Function: cram_mac
 * -----------------
 * enables MAC operation on CRAM on all active tiles
 *
 *
 * returns: void
 */
void cram_mac();

/* Function: wait_idle
 * -----------------
 * waits for idle status bits
 *
 *
 * returns: void
 */
void wait_idle();

/* Function: wait_finished
 * -----------------
 * waits for finished status bits
 *
 *
 * returns: void
 */
void wait_finished();

/* Function: enable_MC
 * -----------------
 * enables the Memory Controller
 *
 *
 * returns: void
 */
void enable_MC();


void CHECKPOINT(void);


#endif /* VIADOTTO_H_ */
