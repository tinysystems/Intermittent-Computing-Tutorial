----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    20:43:48 10/05/2022 
-- Design Name: 
-- Module Name:    PTR_reg5_1 - Behavioral 
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

entity PTR_reg5_1 is
    Port ( I_clk : in  STD_LOGIC;
           I_en : in  STD_LOGIC;
           I_ptr_incr : in  STD_LOGIC_VECTOR (4 downto 0);
			  O_ptr_incr : out  STD_LOGIC_VECTOR (4 downto 0);
           O_ptr_buff : out  STD_LOGIC_VECTOR (4 downto 0);
			  O_ptr_cmp : out  STD_LOGIC_VECTOR (4 downto 0));
end PTR_reg5_1;

architecture Behavioral of PTR_reg5_1 is

begin
	process(I_clk, I_en)
	begin
		if rising_edge(I_clk) and I_en='1' then
			O_ptr_buff <= I_ptr_incr;
			O_ptr_cmp <= I_ptr_incr;
			O_ptr_incr <= I_ptr_incr;
		end if;
	end process;

end Behavioral;

