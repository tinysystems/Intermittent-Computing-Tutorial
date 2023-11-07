----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    20:41:04 10/05/2022 
-- Design Name: 
-- Module Name:    SB_reg2_1 - Behavioral 
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

entity SB_reg2_1 is
    Port ( I_clk : in  STD_LOGIC;
           I_en : in  STD_LOGIC;
           I_sb : in  STD_LOGIC_VECTOR (1 downto 0);
			  I_sb_cm : in  STD_LOGIC_VECTOR (1 downto 0);
           O_sb : out  STD_LOGIC_VECTOR (1 downto 0));
end SB_reg2_1;

architecture Behavioral of SB_reg2_1 is

begin

	process(I_clk)
	begin
		if rising_edge(I_clk) then
			if I_en='1' then
				O_sb <= I_sb;
			else
				O_sb <= I_sb_cm;
			end if;
		end if;
	end process;
end Behavioral;

