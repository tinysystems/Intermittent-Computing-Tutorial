----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    20:39:36 10/05/2022 
-- Design Name: 
-- Module Name:    EN_out_reg1_1 - Behavioral 
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

entity EN_out_reg1_1 is
    Port ( I_clk : in  STD_LOGIC;
           I_en : in  STD_LOGIC;
			  I_en_cm : in  STD_LOGIC;
           I_eno : in  STD_LOGIC;
           O_eno : out  STD_LOGIC);
end EN_out_reg1_1;

architecture Behavioral of EN_out_reg1_1 is

begin
	process(I_clk, I_en, I_en_cm)
	begin
		if rising_edge(I_clk) and (I_en='1' or I_en_cm='1') then
			O_eno <= I_eno;
		end if;
	end process;

end Behavioral;

