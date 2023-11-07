----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    20:29:07 10/05/2022 
-- Design Name: 
-- Module Name:    adr_reg16_1 - Behavioral 
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

entity adr_reg16_1 is
    Port ( I_clk : in  STD_LOGIC;
           I_en : in  STD_LOGIC;
			  I_en_incr : in STD_LOGIC;
           I_a_cpu : in  STD_LOGIC_VECTOR (15 downto 0);
			  I_a_incr : in STD_LOGIC_VECTOR (15 downto 0);
           O_a_incr : out  STD_LOGIC_VECTOR (15 downto 0);
			  O_a_uct : out  STD_LOGIC_VECTOR (15 downto 0));
end adr_reg16_1;

architecture Behavioral of adr_reg16_1 is

begin

	process(I_clk, I_en)
	begin
		if rising_edge(I_clk) and I_en='1' then
			if I_en='1' then
				O_a_uct <= I_a_cpu;
				O_a_incr <= I_a_cpu;
			end if;
			if I_en_incr='1' then
				O_a_uct <= I_a_incr;
				O_a_incr <= I_a_incr;
			end if;
		end if;
	end process;

end Behavioral;

