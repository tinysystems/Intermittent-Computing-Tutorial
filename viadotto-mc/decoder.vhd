----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    10:35:44 10/07/2022 
-- Design Name: 
-- Module Name:    decoder - Behavioral 
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

entity decoder is
    Port ( I_clk : in  STD_LOGIC;
           I_en : in  STD_LOGIC;
           I_instr : in  STD_LOGIC_VECTOR (63 downto 0); --two MSBs are reserved and not used
           O_en : out  STD_LOGIC;
           O_lbl : out  STD_LOGIC;
           O_d : out  STD_LOGIC;
           O_we : out  STD_LOGIC;
           O_s : out  STD_LOGIC_VECTOR (1 downto 0);
           O_sb : out  STD_LOGIC_VECTOR (1 downto 0);
           O_r0 : out  STD_LOGIC_VECTOR (8 downto 0);
           O_r1 : out  STD_LOGIC_VECTOR (8 downto 0);
           O_r2 : out  STD_LOGIC_VECTOR (8 downto 0);
           O_r3 : out  STD_LOGIC_VECTOR (8 downto 0);
           O_r4 : out  STD_LOGIC_VECTOR (8 downto 0);
           O_r5 : out  STD_LOGIC_VECTOR (8 downto 0));
end decoder;

architecture Behavioral of decoder is

begin
	process(I_clk, I_en)
	begin
		if rising_edge(I_clk) and I_en='1' then
			O_en <= I_instr(61);
			O_lbl <= I_instr(60);
			O_d <= I_instr(59);
			O_we <= I_instr(58);
			O_s <= I_instr(57 downto 56);
			O_sb <= I_instr(55 downto 54);
			O_r0 <= I_instr(53 downto 45);
			O_r1 <= I_instr(44 downto 36);
			O_r2 <= I_instr(35 downto 27);
			O_r3 <= I_instr(26 downto 18);
			O_r4 <= I_instr(17 downto 9);
			O_r5 <= I_instr(8 downto 0);
			
		end if;
	end process;


end Behavioral;

