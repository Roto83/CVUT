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

## Embedded Files
4f1cc100a112ff64488bc8585fa5157c42c75153: [[Pasted image 20261125140645.png]]

%%
## Drawing
```compressed-json
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

hwgx0y1CAEtRAA==
```
%%