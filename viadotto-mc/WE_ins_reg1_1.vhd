----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    12:25:17 10/06/2022 
-- Design Name: 
-- Module Name:    WE_ins_reg1_1 - Behavioral 
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

entity WE_ins_reg1_1 is
    Port ( I_clk : in  STD_LOGIC;
           I_we : in  STD_LOGIC;
           O_we : out  STD_LOGIC;
			  O_we_dir : out  STD_LOGIC);
end WE_ins_reg1_1;

architecture Behavioral of WE_ins_reg1_1 is

begin
	process(I_clk)
	begin
		if rising_edge(I_clk) then
			O_we <= I_we;
			O_we_dir <= I_we;
		end if;
	end process;

end Behavioral;

