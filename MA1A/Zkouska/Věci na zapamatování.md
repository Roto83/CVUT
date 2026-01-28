### Derivace
##### L'Hospitalovo pravidlo
Děláme derivace prostě a jdenoduše. Derivujeme zlomek zvlášť a ne podle pravidla.
##### Taylorův polynom
$$
\sum ^{n}_{k=0} \frac{f^{(k)}(a)}{k!}(x-a)^{k}
$$
### Posloupnost
Funkce ale má jen přirozená čísla, je tedy nespojitá a má jen tečky. Může být ne/rostoucí či ne/klesající. Zjistíme tak že dáme (n+1) a odečteme od něj předchozí a porovnáváme kladný výsledek = rostoucí, záporný klesající.
##### Limita posloupnosti
Pokud vyjde vlastní číslo tak je konvergentní. Pokud vyjde v nekonečnu, nebo kmitá, je divergentní. Limita se počítá jen v nekonečnu, jinak by se muselo říct že si posloupnost převedeme na funkci. Teprve pak jde taky používat L'Hospital.
##### Geometrická posloupnost
n je v exponentu. Pokud po vytknutí máme zlomek menší než 1 je to 0, když naopak tak nekonečno.
### Číselné řady
Narozdíl od posloupnosti je to součet všech těch čísel. Pokud konverguje má konečný součet, pokud diverguje má nekonečný součet.
##### Geometrická řada
Vždy ve tvaru: $\sum^{\infty}_{n=1}a\cdot q^{n-1}$ (číslo . zlomek na n). Pokud $|q|<1$ konverguje a sečteme ji pomocí $S=\frac{a_{1}}{1-q}$ . Pokud $|q|>1$ diverguje a sečíst nelze. Je možné že budou i dvě v sobě. Pak musíme ve finále jejich součty sečíst nebo odečíst podle znaménka.

##### Harmonická řada
Ve tvaru: $\sum^{\infty}_{n=1} \frac{1}{n}=1 + \frac{1}{2} + \frac{1}{4}+\dots$ a vždy diverguje i když vyjde limita nula.
##### Postup a kritéria
1) Zkusit limitu n jde do nekonečna. Vyjde něco jiného než 0 a diverguje.
2) Pokud tam je faktoriál a něco na n-tou, dám podílové kritérium. $\frac{a_{n+1}}{a_{n}}$ dám do limity. Když vyjde $L<1$ tak konverguje, $L>1$ diverguje. $L=1$ nevíme.
3) Pokud je to celé umocněné, tak si ji odmyslím a počítám limitu bez ní. Když vyjde $L<1$ tak konverguje, $L>1$ diverguje. $L=1$ nevíme.
4) Pokud tam máme jen polynomy, srovnáváme s $\frac{1}{n^{k}}$. Když je $k\leq1$ tak diverguje, $k>1$ konverguje.
5) Když se někde nachází $(-1)^{n}$ je to Leibnizovo kritérium. Odmyslíme si to znaménko a zkusíme 1). Pak musí klesat, pokud to nepůjde dokázat jednoduše můžeme to udělat derivací. V derivaci dosadíme kladné n, pokud vyjde + roste pokud - klesá. Pak musím určit jestli absolutně nebo neabsolutně, nejsilnější členy vezmeme a vydělíme jimi celý zbytek. Pokud limita z tohoto je nějaké číslo a ne 0 nebo nekonečno, konverguje absolutně.


### Vzorce pro grafy
1) Obsah plochy: $$S = \int_{a}^{b} Horní(x) - Dolní(x)$$
2) Objem rotačního tělesa: $$V = \pi \cdot \int_{a}^{b}[f(x)]^{2}dx$$
3)  Délka grafu:$$L = \int_{a}^{b} \sqrt{ 1 + [f'(x)]^{2} } \space dx$$

