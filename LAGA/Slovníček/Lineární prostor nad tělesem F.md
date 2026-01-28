Lineární prostor nad tělesem $\mathbb{F}$ je množina L spolu se dvěma funkcemi:
$+: L \times L \to L, \quad \cdot: \mathbb{F} \times L \to L$

- Vlastnosti sčítání: 
	1) Existuje $\vec{o} \in L$ tak, že pro všechna $\vec{x} \in L$ platí: $\vec{x} + \vec{o} = \vec{o} + \vec{x} = \vec{x}$ (**existence nulového vektoru**)
	2) Pro všechna $\vec{x}, \vec{y}, \vec{z} \in L$ platí: $(\vec{x} + \vec{y}) + \vec{z} = \vec{x} + (\vec{y} +\vec{z})$ (**asociativita sčítání vektorů, nezáleží jak jsou při sčítání uskupené v závorkách**). 
	3) Pro všechna $\vec{x}, \vec{y} \in L$ platí: $\vec{x} + \vec{y} = \vec{y} + \vec{x}$ (**komutativita sčítání vektorů, nezáleží na pořadí sčítání**). 
	4) Pro všechna $\vec{x} \in L$ existuje právě jeden $\vec{y} \in L$ tak, že $\vec{x} + \vec{y} = \vec{o}$  (**existence opačného vektoru** $\vec{y} = -\vec{x}$). 

- Vlastnsoti násobení skalárem:
	1)  Pro všechna $\vec{x}\in L$ platí: $1 \cdot \vec{x} = \vec{x}$ (**násobení jednotkovým skalárem**)
	2) Pro všechna $a, b \in \mathbb{F}$ a všechna $\vec{x} \in L$ platí: $a \cdot (b \cdot \vec{x}) = (a \cdot b) \cdot \vec{x}$ (**asociativita násobení vektorů, nezáleží jak jsou při násobení uskupené v závorkách**)

- Distributivní zákony (pravidla roznásobení závorek):
	1) Pro všechna $a,b \in \mathbb{F}$ a všechna $\vec{x} \in L$ platí: $(a+b) \cdot \vec{x} = a \cdot \vec{x} + b \cdot \vec{x}$ (**distributivita součtu skalárů, jako normálně**)
	2) Pro všechna $a \in \mathbb{F}$ a všechna $\vec{x}, \vec{y} \in L$ platí: $a \cdot(\vec{x}+\vec{y}) = a \cdot \vec{x} + a \cdot \vec{y}$ (**distributivita součtu vektorů, jako normálně**) 
### Intuitivně:
Stejné jako [[Lineární prostor nad R]] akorát nad tělesem $\mathbb{F}$, tedy obecněji.