----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    12:58:19 10/06/2022 
-- Design Name: 
-- Module Name:    R_ins_reg9_1 - Behavioral 
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

entity R_ins_reg9_1 is
    Port ( I_clk : in  STD_LOGIC;
           I_row : in  STD_LOGIC_VECTOR (8 downto 0);
           O_row : out  STD_LOGIC_VECTOR (8 downto 0));
end R_ins_reg9_1;

architecture Behavioral of R_ins_reg9_1 is

begin
	process(I_clk)
	begin
		if rising_edge(I_clk) then
			O_row <= I_row;
		end if;
	end process;

end Behavioral;

