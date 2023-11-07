----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    21:46:27 10/06/2022 
-- Design Name: 
-- Module Name:    incrementor - Behavioral 
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

entity incrementor_a is
    Port ( I_clk : in  STD_LOGIC;
           I_en : in  STD_LOGIC_VECTOR (1 downto 0);
			  I_en_cmp : in  STD_LOGIC;
           I_addr : in  STD_LOGIC_VECTOR (15 downto 0);
			  O_en : out STD_LOGIC;
           O_next_addr : out  STD_LOGIC_VECTOR (15 downto 0));
end incrementor_a;

architecture Behavioral of incrementor_a is

begin
	process(I_clk, I_en, I_en_cmp)
	begin
		if rising_edge(I_clk) and ((I_en(0)='1' and I_en(1)='1') or I_en_cmp='1') then
			O_next_addr <= std_logic_vector( unsigned(I_addr) + 1 );
			O_en <= '1';
		end if;
	end process;

end Behavioral;

