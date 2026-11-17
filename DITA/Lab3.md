---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
architecture Behavioral_with_select of adder is
    signal vstup  : std_logic_vector(2 downto 0);
    signal vystup : std_logic_vector(1 downto 0); -- vystup(1) = cout, vystup(0) = s
begin
    vstup <= cin & b & a;

    with vstup select
        vystup <= "00" when "000",
                  "01" when "001" | "010" | "100",
                  "10" when "011" | "101" | "110",
                  "11" when "111",
                  "XX" when others;

    cout <= vystup(1);
    s    <= vystup(0);
end Behavioral_with_select; ^Sj6LFL4r

select/when ^cgNQuQFu

when/else ^dTDopAS3

if/else ^gFTyiOrS

case ^S3jhbGF5

architecture Behavioral_when_else of adder is
    signal vstup  : std_logic_vector(2 downto 0);
    signal vystup : std_logic_vector(1 downto 0);
begin
    vstup <= cin & b & a;

    vystup <= "00" when vstup = "000" else
              "01" when (vstup = "001" or vstup = "010" or vstup = "100") else
              "10" when (vstup = "011" or vstup = "101" or vstup = "110") else
              "11" when vstup = "111" else
              "XX";

    cout <= vystup(1);
    s    <= vystup(0);
end Behavioral_when_else; ^yXlWSiBX

architecture Behavioral_if of adder is
begin
    process(a, b, cin)
    begin
        if (cin = '0' and b = '0' and a = '0') then
            cout <= '0'; s <= '0';
        elsif ((cin = '0' and b = '0' and a = '1') or
               (cin = '0' and b = '1' and a = '0') or
               (cin = '1' and b = '0' and a = '0')) then
            cout <= '0'; s <= '1';
        elsif ((cin = '0' and b = '1' and a = '1') or
               (cin = '1' and b = '0' and a = '1') or
               (cin = '1' and b = '1' and a = '0')) then
            cout <= '1'; s <= '0';
        elsif (cin = '1' and b = '1' and a = '1') then
            cout <= '1'; s <= '1';
        else
            cout <= 'X'; s <= 'X';
        end if;
    end process;
end Behavioral_if; ^HsU21QXs

architecture Behavioral_case of adder is
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
end Behavioral_case; ^4hfDLX1m

1) ^buzLecje

2) ^yZohOJix

architecture Dataflow_RTL of adder is
begin
    s    <= a xor b xor cin;
    cout <= (a and b) or (cin and (a xor b));
end Dataflow_RTL; ^0vNJAKxp

architecture Bonus_Arithmetic of adder is
    signal soucet : std_logic_vector(1 downto 0);
begin
    soucet <= std_logic_vector(unsigned'('0' & a) + unsigned'('0' & b) + unsigned'('0' & cin));

    cout <= soucet(1);
    s    <= soucet(0);
end Bonus_Arithmetic; ^Gz8cLqXH

%%
## Drawing
```compressed-json
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
```
%%