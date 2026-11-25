library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity adder2 is
    port (A, B : in  std_logic_vector(1 downto 0);
          Cin  : in  std_logic;
          S    : out std_logic_vector(1 downto 0);
          Cout : out std_logic);
end adder2;

architecture Structural of adder2 is
    signal C0 : std_logic := '0'; -- vnitrni vodic pro prenos mezi scitackami[cite: 102, 103]
begin
    -- 1. stupen (LSB): pouzije napr. architekturu RTL[cite: 95, 99, 102]
    prvni : entity work.adder(RTL)
        port map (a    => A(0),
                  b    => B(0),
                  cin  => Cin,
                  s    => S(0),
                  cout => C0);

    -- 2. stupen (MSB): pouzije jinou architekturu, napr. Behavioral_concurrent[cite: 95, 99, 102]
    druha : entity work.adder(Behavioral_concurrent)
        port map (a    => A(1),
                  b    => B(1),
                  cin  => C0,
                  s    => S(1),
                  cout => Cout);
end Structural;