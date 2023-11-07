----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    20:56:07 10/05/2022 
-- Design Name: 
-- Module Name:    DBUF_reg8_32768 - Behavioral 
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

entity DBUF_reg8_32768 is
    Port ( I_clk : in  STD_LOGIC;
           I_en : in  STD_LOGIC;
			  I_we : in STD_LOGIC;
			  I_dir : in STD_LOGIC;
           I_ptr : in  STD_LOGIC_VECTOR (4 downto 0);
           I_data_cpu : in  STD_LOGIC_VECTOR (7 downto 0);
           I_data_reg : in  STD_LOGIC_VECTOR (7 downto 0);
			  O_data_cpu : out  STD_LOGIC_VECTOR (7 downto 0);
           O_data_reg : out  STD_LOGIC_VECTOR (7 downto 0));
end DBUF_reg8_32768;

architecture Behavioral of DBUF_reg8_32768 is
	type store_t is array (0 to 32767) of std_logic_vector(7 downto 0);
	signal regs: store_t := (others => X"00");

begin
	process(I_clk, I_en)
	begin
		if rising_edge(I_clk) and I_en='1' then
			if I_dir = '1' then
				O_data_reg <= regs(to_integer(unsigned(I_ptr)));
			else
				regs(to_integer(unsigned(I_ptr))) <= I_data_reg;
			end if;
			if I_we = '1' then
				regs(to_integer(unsigned(I_ptr))) <= I_data_cpu;
			else
				O_data_cpu <= regs(to_integer(unsigned(I_ptr)));
			end if;
		end if;
	end process;

end Behavioral;

