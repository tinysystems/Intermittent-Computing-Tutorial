----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    19:32:01 10/05/2022 
-- Design Name: 
-- Module Name:    PC_reg16_1 - Behavioral 
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

entity PC_reg16_1 is
    Port ( I_clk : in  STD_LOGIC;
           I_en : in  STD_LOGIC;
			  I_en_incr : in  STD_LOGIC;
           I_PC_cpu : in  STD_LOGIC_VECTOR (15 downto 0);
			  I_PC_incr : in  STD_LOGIC_VECTOR (15 downto 0);
           O_PC_cm : out  STD_LOGIC_VECTOR (15 downto 0);
			  O_PC_incr : out  STD_LOGIC_VECTOR (15 downto 0));
end PC_reg16_1;

architecture Behavioral of PC_reg16_1 is

begin

	process(I_clk, I_en)
	begin
		if rising_edge(I_clk) and I_en='1' then
			if I_en_incr='1' then
				O_PC_cm <= I_PC_incr;
				O_PC_incr <= I_PC_incr;
			else
				O_PC_cm <= I_PC_cpu;
				O_PC_incr <= I_PC_cpu;
			end if;
		end if;
	end process;

end Behavioral;

