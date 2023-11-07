----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    21:59:31 10/06/2022 
-- Design Name: 
-- Module Name:    comparator - Behavioral 
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
use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity comparator is
    Port ( I_clk : in  STD_LOGIC;
           I_en : in  STD_LOGIC_VECTOR (1 downto 0);
			  I_en_cm : in  STD_LOGIC;
           I_a : in  STD_LOGIC_VECTOR (4 downto 0);
           I_b : in  STD_LOGIC_VECTOR (4 downto 0);
           O_en : out  STD_LOGIC);
end comparator;

architecture Behavioral of comparator is

begin
	process(I_clk, I_en, I_en_cm)
	begin
		if rising_edge(I_clk) and ((I_en(0)='1' and I_en(1)='1') or I_en_cm='1') then
			if unsigned(I_a) = (unsigned(I_b) - 1) then
				O_en <= '1';
			else
				O_en <= '0';
			end if;
		end if;
	end process;

end Behavioral;

