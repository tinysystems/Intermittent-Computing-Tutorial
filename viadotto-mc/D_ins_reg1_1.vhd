----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    12:23:11 10/06/2022 
-- Design Name: 
-- Module Name:    D_ins_reg1_1 - Behavioral 
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

entity D_ins_reg1_1 is
    Port ( I_clk : in  STD_LOGIC;
           I_d : in  STD_LOGIC;
           O_d : out  STD_LOGIC);
end D_ins_reg1_1;

architecture Behavioral of D_ins_reg1_1 is

begin
	process(I_clk)
	begin
		if rising_edge(I_clk) then
			O_d <= I_d;
		end if;
	end process;

end Behavioral;

