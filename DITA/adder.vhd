library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.numeric_std.ALL; -- nutne pro bonusovy ukol

entity adder is
    port (a, b, cin : in  std_logic;
          s, cout   : out std_logic);
end adder;

--------------------------------------------------------------------
-- a) when / else
--------------------------------------------------------------------
architecture Behavioral_concurrent of adder is
    signal vstup  : std_logic_vector(2 downto 0);
    signal vystup : std_logic_vector(1 downto 0);
begin
    vstup <= cin & b & a; -- cin = MSB, a = LSB

    vystup <= "00" when vstup = "000" else
              "01" when (vstup = "001" or vstup = "010" or vstup = "100") else
              "10" when (vstup = "011" or vstup = "101" or vstup = "110") else
              "11" when vstup = "111" else
              "XX";

    cout <= vystup(1);
    s    <= vystup(0);
end Behavioral_concurrent;

--------------------------------------------------------------------
-- b) Sekvencni prostredi: case v procesu
--------------------------------------------------------------------
architecture Behavioral_sequential of adder is
    signal vstup : std_logic_vector(2 downto 0);
begin
    vstup <= cin & b & a;

    process(vstup)
    begin
        case vstup is
            when "000" =>
                cout <= '0'; s <= '0';
            when "001" | "010" | "100" =>
                cout <= '0'; s <= '1';
            when "011" | "101" | "110" =>
                cout <= '1'; s <= '0';
            when "111" =>
                cout <= '1'; s <= '1';
            when others =>
                cout <= 'X'; s <= 'X';
        end case;
    end process;
end Behavioral_sequential;

--------------------------------------------------------------------
-- c) Dataflow (RTL) popis pomoci Booleovych rovnic
--------------------------------------------------------------------
architecture RTL of adder is
begin
    s    <= a xor b xor cin;
    cout <= (a and b) or (cin and (a xor b));
end RTL;

--------------------------------------------------------------------
-- d) Bonus: Aritmeticke scitani a konverze typu
--------------------------------------------------------------------
architecture Bonus of adder is
    signal soucet : std_logic_vector(1 downto 0);
begin
    soucet <= std_logic_vector(unsigned'('0' & a) + unsigned'('0' & b) + unsigned'('0' & cin));

    cout <= soucet(1);
    s    <= soucet(0);
end Bonus;