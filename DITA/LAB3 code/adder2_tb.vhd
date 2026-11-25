library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity adder2_tb is
end adder2_tb;

architecture Behavioral of adder2_tb is
    signal a, b, s   : std_logic_vector(1 downto 0);
    signal cin, cout : std_logic;
begin
    uut : entity work.adder2
        port map (A    => a,
                  B    => b,
                  Cin  => cin,
                  S    => s,
                  Cout => cout);

    process
    begin
        wait for 40 ns; -- inicializace[cite: 101]
        a <= "00"; b <= "00"; cin <= '0'; -- 0 + 0 + 0 = 0[cite: 101]
        wait for 40 ns;
        a <= "01"; b <= "00"; cin <= '0'; -- 1 + 0 + 0 = 1
        wait for 40 ns;
        a <= "01"; b <= "01"; cin <= '0'; -- 1 + 1 + 0 = 2 (test vnitrniho prenosu C0)
        wait for 40 ns;
        a <= "10"; b <= "01"; cin <= '0'; -- 2 + 1 + 0 = 3
        wait for 40 ns;
        a <= "10"; b <= "10"; cin <= '0'; -- 2 + 2 + 0 = 4 (test Cout)
        wait for 40 ns;
        a <= "11"; b <= "01"; cin <= '1'; -- 3 + 1 + 1 = 5 (prenos pres oba stupne)
        wait for 40 ns;
        a <= "11"; b <= "11"; cin <= '0'; -- 3 + 3 + 0 = 6
        wait for 40 ns;
        a <= "11"; b <= "11"; cin <= '1'; -- 3 + 3 + 1 = 7 (maximalni hodnota)
        wait for 40 ns;
        a <= "00"; b <= "11"; cin <= '1'; -- 0 + 3 + 1 = 4
        wait for 40 ns;
        wait; -- zastaveni simulace[cite: 101]
    end process;
end Behavioral;