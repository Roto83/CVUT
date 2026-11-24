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

%%
## Drawing
```compressed-json
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
```
%%