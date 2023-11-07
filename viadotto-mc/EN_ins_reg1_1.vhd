----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    12:17:17 10/06/2022 
-- Design Name: 
-- Module Name:    EN_ins_reg1_1 - Behavioral 
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

entity EN_ins_reg1_1 is
    Port ( I_clk : in  STD_LOGIC;
           I_eni : in  STD_LOGIC;
           O_eni : out  STD_LOGIC);
end EN_ins_reg1_1;

architecture Behavioral of EN_ins_reg1_1 is

begin
	process(I_clk)
	begin
		if rising_edge(I_clk) then
			O_eni <= I_eni;
		end if;
	end process;

end Behavioral;

