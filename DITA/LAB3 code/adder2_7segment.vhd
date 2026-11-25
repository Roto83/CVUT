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
    zobrazeni(3) <= '0'; -- nejvyssi bit BCD (MSB) je trvale 0 (rozsah vysledku 0-7)[cite: 97, 104]

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
end Structural;