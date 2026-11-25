---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity adder2 is
    port (A, B : in  std_logic_vector(1 downto 0);
          Cin  : in  std_logic;
          S    : out std_logic_vector(1 downto 0);
          Cout : out std_logic);
end adder2;

architecture Structural of adder2 is
    signal C0 : std_logic := '0';
begin
    prvni : entity work.adder(RTL)
        port map (a    => A(0),
                  b    => B(0),
                  cin  => Cin,
                  s    => S(0),
                  cout => C0);

Behavioral_concurrent
    druha : entity work.adder(Behavioral_concurrent)
        port map (a    => A(1),
                  b    => B(1),
                  cin  => C0,
                  s    => S(1),
                  cout => Cout);
end Structural; ^VyYPOtSq

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
        wait for 40 ns;
        a <= "00"; b <= "00"; cin <= '0';
        wait for 40 ns;
        a <= "01"; b <= "00"; cin <= '0';
        wait for 40 ns;
        a <= "01"; b <= "01"; cin <= '0';
        wait for 40 ns;
        a <= "10"; b <= "01"; cin <= '0';
        wait for 40 ns;
        a <= "10"; b <= "10"; cin <= '0';
        wait for 40 ns;
        a <= "11"; b <= "01"; cin <= '1';
        wait for 40 ns;
        a <= "11"; b <= "11"; cin <= '0';
        wait for 40 ns;
        a <= "11"; b <= "11"; cin <= '1';
        wait for 40 ns;
        a <= "00"; b <= "11"; cin <= '1';
        wait for 40 ns;
        wait;
    end process;
end Behavioral; ^B0k2YgoL

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity adder2_7segment is
    port (A, B                   : in  std_logic_vector(1 downto 0);
          Cin                    : in  std_logic;
          s0, s1, s2, s3, s4, s5, s6 : out std_logic);
end adder2_7segment;

architecture Structural of adder2_7segment is
    signal zobrazeni : std_logic_vector(3 downto 0) := "0000";
begin
    zobrazeni(3) <= '0';
    scitacka : entity work.adder2
        port map (A    => A,
                  B    => B,
                  Cin  => Cin,
                  S    => zobrazeni(1 downto 0),
                  Cout => zobrazeni(2));

    displej : entity work.BCD7segmentVHDL
        port map (a  => zobrazeni(0),
                  b  => zobrazeni(1),
                  c  => zobrazeni(2),
                  d  => zobrazeni(3),
                  s0 => s0,
                  s1 => s1,
                  s2 => s2,
                  s3 => s3,
                  s4 => s4,
                  s5 => s5,
                  s6 => s6);
end Structural; ^pZSxQ0UX

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity adder2_7segment is
    port (A, B                         : in  std_logic_vector(1 downto 0);
          Cin                          : in  std_logic;
          -- Vystup vysledku souctu (HEX0)
          s0, s1, s2, s3, s4, s5, s6   : out std_logic;
          -- Vystup pro zobrazeni scitance A (HEX1)
          sA0, sA1, sA2, sA3, sA4, sA5, sA6 : out std_logic;
          -- Vystup pro zobrazeni scitance B (HEX2)
          sB0, sB1, sB2, sB3, sB4, sB5, sB6 : out std_logic);
end adder2_7segment;

architecture Structural of adder2_7segment is
    signal zobrazeni : std_logic_vector(3 downto 0) := "0000";
begin
    zobrazeni(3) <= '0'; -- nejvyssi bit vysledku (rozsah 0-7)[cite: 104]

    -- 1. Blok 2bitove scitacky[cite: 104]
    scitacka : entity work.adder2
        port map (A    => A,
                  B    => B,
                  Cin  => Cin,
                  S    => zobrazeni(1 downto 0),
                  Cout => zobrazeni(2));

    -- 2. Displej pro vysledek souctu (HEX0)[cite: 104]
    displej_soucet : entity work.BCD7segmentVHDL
        port map (a  => zobrazeni(0), b  => zobrazeni(1),
                  c  => zobrazeni(2), d  => zobrazeni(3),
                  s0 => s0, s1 => s1, s2 => s2, s3 => s3,
                  s4 => s4, s5 => s5, s6 => s6);

    -- 3. Displej pro scitanec A (HEX1)
    displej_A : entity work.BCD7segmentVHDL
        port map (a  => A(0), b  => A(1),
                  c  => '0',  d  => '0',
                  s0 => sA0, s1 => sA1, s2 => sA2, s3 => sA3,
                  s4 => sA4, s5 => sA5, s6 => sA6);

    -- 4. Displej pro scitanec B (HEX2)
    displej_B : entity work.BCD7segmentVHDL
        port map (a  => B(0), b  => B(1),
                  c  => '0',  d  => '0',
                  s0 => sB0, s1 => sB1, s2 => sB2, s3 => sB3,
                  s4 => sB4, s5 => sB5, s6 => sB6);
end Structural; ^lqsbleBU

%%
## Drawing
```compressed-json
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

r9ByggDgB9Si9EUOEH/GWoQAlqIAA===
```
%%