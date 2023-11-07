----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    10:32:00 10/07/2022 
-- Design Name: 
-- Module Name:    configurator - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity configurator is
  Port (	I_clk : in STD_LOGIC;
			I_en : in STD_LOGIC;
			I_we_drf : in STD_LOGIC;
			I_we : in STD_LOGIC_VECTOR (1 downto 0);
			I_tile_id : in STD_LOGIC_VECTOR (4 downto 0);
			I_data_size : in STD_LOGIC_VECTOR (4 downto 0);
			I_row_addr : in STD_LOGIC_VECTOR (15 downto 0);
			I_pc : in STD_LOGIC_VECTOR (15 downto 0);
			I_sb : in STD_LOGIC_VECTOR (1 downto 0);
			I_data_cpu : in STD_LOGIC_VECTOR (7 downto 0);
			O_data_cpu : out STD_LOGIC_VECTOR (7 downto 0);
			O_row_addr : out STD_LOGIC_VECTOR (15 downto 0);
			O_tile_id : out STD_LOGIC_VECTOR (4 downto 0);
			I_data_uct : in STD_LOGIC_VECTOR (7 downto 0);
			O_data_uct : out STD_LOGIC_VECTOR (7 downto 0);
			O_sb : out STD_LOGIC_VECTOR (1 downto 0);
			O_en : out STD_LOGIC;
			O_lbl : out STD_LOGIC;
			O_d : out STD_LOGIC;
			O_we : out STD_LOGIC;
			O_s : out STD_LOGIC_VECTOR (1 downto 0);
			O_r0 : out STD_LOGIC_VECTOR (8 downto 0);
			O_r1 : out STD_LOGIC_VECTOR (8 downto 0);
			O_r2 : out STD_LOGIC_VECTOR (8 downto 0);
			O_r3 : out STD_LOGIC_VECTOR (8 downto 0);
			O_r4 : out STD_LOGIC_VECTOR (8 downto 0);
			O_r5 : out STD_LOGIC_VECTOR (8 downto 0)
  
  );
end configurator;

architecture Structural of configurator is

	signal PTR_BUFF : STD_LOGIC_VECTOR (4 downto 0);
	signal PTR_CMP : STD_LOGIC_VECTOR (4 downto 0);
	signal DATAIN : STD_LOGIC_VECTOR (7 downto 0); --input from CPU
	signal DATAOUT : STD_LOGIC_VECTOR (7 downto 0); --output to CPU
	signal DIR : STD_LOGIC;
	signal EN : STD_LOGIC;
	--signal CONFMEM_INCR_B_EN : STD_LOGIC;
	signal PTR_INCR_B_IN : STD_LOGIC_VECTOR (4 downto 0);
	signal PTR_INCR_B_OUT : STD_LOGIC_VECTOR (4 downto 0);
	signal PTR_INCR_B_EN : STD_LOGIC;
	signal ADDR_INCR_B_IN : STD_LOGIC_VECTOR (15 downto 0);
	signal ADDR_INCR_B_OUT : STD_LOGIC_VECTOR (15 downto 0);
	signal ADDR_INCR_B_EN : STD_LOGIC;
	signal PC_CONFMEM : STD_LOGIC_VECTOR (15 downto 0);
	signal CMP_INCR_A_EN : STD_LOGIC;
	signal PC_INCR_A_IN : STD_LOGIC_VECTOR (15 downto 0);
	signal PC_INCR_A_OUT : STD_LOGIC_VECTOR (15 downto 0);
	signal PC_INCR_A_EN : STD_LOGIC;
	signal SIZE_CMP : STD_LOGIC_VECTOR (4 downto 0);
	signal WE_INCR_A : STD_LOGIC_VECTOR (1 downto 0);
	signal WE_INCR_B : STD_LOGIC_VECTOR (1 downto 0);
	signal WE_INCR_CMP : STD_LOGIC_VECTOR (1 downto 0);
	signal EN_CONFMEM_IN : STD_LOGIC;
	signal EN_CONFMEM_OUT : STD_LOGIC;
	signal EN_DECODE : STD_LOGIC;
	signal CM_DECODE : STD_LOGIC_VECTOR (63 downto 0);
	signal CM_SB : STD_LOGIC_VECTOR (1 downto 0);
	signal DECODE_EN : STD_LOGIC;
	signal DECODE_LBL : STD_LOGIC;
	signal DECODE_D : STD_LOGIC;
	signal DECODE_WE : STD_LOGIC;
	signal DECODE_S : STD_LOGIC_VECTOR (1 downto 0);
	signal DECODE_SB : STD_LOGIC_VECTOR (1 downto 0);
	signal DECODE_R0 : STD_LOGIC_VECTOR (8 downto 0);
	signal DECODE_R1 : STD_LOGIC_VECTOR (8 downto 0);
	signal DECODE_R2 : STD_LOGIC_VECTOR (8 downto 0);
	signal DECODE_R3 : STD_LOGIC_VECTOR (8 downto 0);
	signal DECODE_R4 : STD_LOGIC_VECTOR (8 downto 0);
	signal DECODE_R5 : STD_LOGIC_VECTOR (8 downto 0);


begin
	set_bit_register : entity work.SB_reg2_1
		port map(
			I_clk => I_clk,
			I_en => I_en,
			I_sb => I_sb,
			I_sb_cm => CM_SB,
			O_sb => O_sb
		);
	data_rf : entity work.DBUF_reg8_32768
		port map(
			I_clk => I_clk,
			I_en => I_en,
			I_we => I_we_drf,
			I_dir => DIR,
			I_ptr => PTR_BUFF,
			I_data_cpu => I_data_cpu,
			O_data_cpu => O_data_cpu,
			I_data_reg => DATAOUT,
			O_data_reg => DATAIN
		);
	data_buff : entity work.DBUF_reg8_1
		port map(
			I_clk => I_clk,
			I_en => I_en,
			I_dir => DIR,
			I_data_buff => DATAIN,
			O_data_buff => DATAOUT,
			I_data_uct => I_data_uct,
			O_data_uct => O_data_uct
		);
	ptr_reg : entity work.PTR_reg5_1
		port map(
			I_clk => I_clk,
			I_en => EN_CONFMEM_IN,
			I_ptr_incr => PTR_INCR_B_IN,
			O_ptr_incr => PTR_INCR_B_OUT,
			O_ptr_buff => PTR_BUFF,
			O_ptr_cmp => PTR_CMP
		);
	pc_reg : entity work.PC_reg16_1
		port map(
			I_clk => I_clk,
			I_en => I_en,
			I_en_incr => PC_INCR_A_EN,
			I_PC_cpu => I_pc,
			I_PC_incr => PC_INCR_A_IN,
			O_PC_cm => PC_CONFMEM,
			O_PC_incr => PC_INCR_A_OUT
		);
	addr_reg : entity work.adr_reg16_1
		port map(
			I_clk => I_clk,
			I_en => I_en,
			I_en_incr => ADDR_INCR_B_EN,
			I_a_cpu => I_row_addr,
			I_a_incr => ADDR_INCR_B_IN,
			O_a_incr => ADDR_INCR_B_OUT,
			O_a_uct => O_row_addr
		);
	size_reg : entity work.size_reg5_1
		port map(
			I_clk => I_clk,
			I_en => I_en,
			I_size => I_data_size,
			O_size => SIZE_CMP
		);
	tile_reg : entity work.tile_reg5_1
		port map(
			I_clk => I_clk,
			I_en => I_en,
			I_tile => I_tile_id,
			O_tile => O_tile_id
		);
	we_out_reg : entity work.WE_out_reg2_1
		port map(
			I_clk => I_clk,
			I_en => I_en,
			I_weo => I_we,
			O_weo => WE_INCR_A
		);
	en_out_reg : entity work.EN_out_reg1_1
		port map(
			I_clk => I_clk,
			I_en => I_en,
			I_en_cm => EN_CONFMEM_IN,
			I_eno => I_en,
			O_eno => EN_CONFMEM_OUT
		);
	incr_a : entity work.incrementor_a
		port map(
			I_clk => I_clk,
			I_en => WE_INCR_A,
			I_en_cmp => CMP_INCR_A_EN,
			I_addr => PC_INCR_A_OUT,
			O_en => PC_INCR_A_EN,
			O_next_addr => PC_INCR_A_IN
		);
	incr_b : entity work.incrementor_b
		port map(
			I_clk => I_clk,
			I_en => WE_INCR_A,
			I_en_cm => DIR,
			I_ptr => PTR_INCR_B_OUT,
			I_addr => ADDR_INCR_B_OUT,
			O_en => ADDR_INCR_B_EN,
			O_next_ptr => PTR_INCR_B_IN,
			O_next_addr => ADDR_INCR_B_IN
		);
	comparator : entity work.comparator
		port map(
			I_clk => I_clk,
			I_en => WE_INCR_A,
			I_en_cm => DIR,
			I_a => PTR_CMP,
			I_b => SIZE_CMP,
			O_en => CMP_INCR_A_EN
		);
	conf_mem : entity work.CM_reg64_1024
		port map(
			I_clk => I_clk,
			I_en => EN_CONFMEM_OUT,
			I_pc => PC_CONFMEM,
			O_instr => CM_DECODE
		);
	decoder : entity work.decoder
		port map(
			I_clk => I_clk,
         I_en => EN_CONFMEM_OUT,
         I_instr => CM_DECODE,
         O_en => DECODE_EN,
         O_lbl => DECODE_LBL,
         O_d => DECODE_D,
         O_we => DECODE_WE,
         O_s => DECODE_S,
         O_sb => DECODE_SB,
         O_r0 => DECODE_R0,
         O_r1 => DECODE_R1,
         O_r2 => DECODE_R2,
         O_r3 => DECODE_R3,
         O_r4 => DECODE_R4,
         O_r5 => DECODE_R5
		);
	en_reg : entity work.EN_ins_reg1_1
		port map(
			I_clk => I_clk,
			I_eni => DECODE_EN,
			O_eni => EN_CONFMEM_IN
		);
	lbl_reg : entity work.LBL_ins_reg1_1
		port map(
			I_clk => I_clk,
			I_lbl => DECODE_LBL,
			O_lbl => O_lbl
		);
	d_reg : entity work.D_ins_reg1_1
		port map(
			I_clk => I_clk,
			I_d => DECODE_D,
			O_d => O_d
		);
	we_reg : entity work.WE_ins_reg1_1
		port map(
			I_clk => I_clk,
			I_we => DECODE_WE,
			O_we => O_we,
			O_we_dir => DIR
		);
	s_reg : entity work.s_ins_reg2_1
		port map(
			I_clk => I_clk,
			I_s => DECODE_S,
			O_s => O_s
		);
	sb_reg : entity work.SB_ins_reg2_1
		port map(
			I_clk => I_clk,
			I_sb => DECODE_SB,
			O_sb => CM_SB
		);
	r0_reg : entity work.R_ins_reg9_1
		port map(
			I_clk => I_clk,
			I_row => DECODE_R0,
			O_row => O_r0
		);
	r1_reg : entity work.R_ins_reg9_1
		port map(
			I_clk => I_clk,
			I_row => DECODE_R1,
			O_row => O_r1
		);
	r2_reg : entity work.R_ins_reg9_1
		port map(
			I_clk => I_clk,
			I_row => DECODE_R2,
			O_row => O_r2
		);
	r3_reg : entity work.R_ins_reg9_1
		port map(
			I_clk => I_clk,
			I_row => DECODE_R3,
			O_row => O_r3
		);
	r4_reg : entity work.R_ins_reg9_1
		port map(
			I_clk => I_clk,
			I_row => DECODE_R4,
			O_row => O_r4
		);
	r5_reg : entity work.R_ins_reg9_1
		port map(
			I_clk => I_clk,
			I_row => DECODE_R5,
			O_row => O_r5
		);
end Structural;

