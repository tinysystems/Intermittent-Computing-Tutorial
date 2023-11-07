----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    07:29:50 10/06/2022 
-- Design Name: 
-- Module Name:    CM_reg32_1024 - Behavioral 
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

entity CM_reg64_1024 is
    Port ( I_clk : in  STD_LOGIC;
           I_en : in  STD_LOGIC;
           I_pc : in  STD_LOGIC_VECTOR (15 downto 0);
           O_instr : out  STD_LOGIC_VECTOR (63 downto 0));
end CM_reg64_1024;

architecture Behavioral of CM_reg64_1024 is
	type store_t is array (0 to 1024) of std_logic_vector(63 downto 0);
	signal regs: store_t := (others => X"0000000000000000");
begin
	process(I_clk, I_en)
	begin
		if rising_edge(I_clk) and I_en='1' then
			O_instr <= regs(to_integer(unsigned(I_pc)));
		end if;
	end process;

end Behavioral;

