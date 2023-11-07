----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    12:19:56 10/06/2022 
-- Design Name: 
-- Module Name:    LBL_ins_reg1_1 - Behavioral 
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

entity LBL_ins_reg1_1 is
    Port ( I_clk : in  STD_LOGIC;
           I_lbl : in  STD_LOGIC;
           O_lbl : out  STD_LOGIC);
end LBL_ins_reg1_1;

architecture Behavioral of LBL_ins_reg1_1 is

begin
	process(I_clk)
	begin
		if rising_edge(I_clk) then
			O_lbl <= I_lbl;
		end if;
	end process;

end Behavioral;

