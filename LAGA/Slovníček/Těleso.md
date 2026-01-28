Těleso je množina $\mathbb{F}$, vybavená dvěma funkcemi:
$+: \mathbb{F} \times \mathbb{F} \to \mathbb{F}, \quad \cdot: \mathbb{F} \times \mathbb{F} \to \mathbb{F}$

- Vlastnosti sčítání: 
	1) Existuje $0 \in \mathbb{F}$ tak, že pro všechna $a \in \mathbb{F}$ platí: $a + 0 = 0 + a = a$ (**existence nuly**)
	2) Pro všechna $a, b, c \in \mathbb{F}$ platí: $(a + b) + c = a + (b +c)$ (**asociativita sčítání, nezáleží jak jsou při sčítání uskupené v závorkách**).
	3) Pro všechna $a, b \in \mathbb{F}$ platí: $a + b = b + a$ (**komutativita sčítání, nezáleží na pořadí sčítání**). 
	4) Pro všechna $a \in \mathbb{F}$ existuje právě jedeno $b \in \mathbb{F}$ tak, že $a + b = 0$  (**existence opačného čísla $b = -a$). 

- Vlastnsoti násobení:
	1) Existuje $1\in \mathbb{F}$ tak, že pro všechna $a \in \mathbb{F}$ platí: $1 \cdot a = a$ (**existence jednotky**)
	2) Pro všechna $a, b, c \in \mathbb{F}$ platí: $a \cdot (b \cdot c) = (a \cdot b) \cdot c$ (**asociativita násobení, nezáleží jak jsou při násobení uskupené v závorkách**)
	3) Pro všechna $a,b \in \mathbb{F}$ platí: $a \cdot b = b \cdot a$ (**komutativita násobení, nezáleží na pořadí v násobení**)

- Provázanost sčítání a násobení:
	1) Pro všechna $a,b,c \in \mathbb{F}$ platí: $a \cdot (b + c) = a \cdot b + a \cdot c$ (levý distributivní zákon)
	2) Pro všechna $a,b,c \in \mathbb{F}$ platí: $(b + c) \cdot a = b \cdot a + c \cdot a$  (pravý distributivní zákon) 

- Test invertibility:
	1) Pro všechna $a \in \mathbb{F}$ platí: $a \neq 0$ právě tehdy, když $a^{-1}$
### Intuitivně:
To podobné jako [[Lineární prostor nad R]] akorát se jedná o sadu čísel, ne vektorů. Je zde navíc komutativita násobení a test invertibility. Hodnota $p$ v $\mathbb{Z}_{p}$ musí být prvočíslo, aby $\mathbb{Z}_{p}$ mohlo být těleso. V například $\mathbb{Z}_{5}$ se hodnoty opakují jako zbytek po dělení 10 = 0, 11 = 1 (číslo $p$ funguje jako modulo v programování)