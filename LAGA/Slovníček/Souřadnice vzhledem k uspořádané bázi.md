Ať [[Seznam|seznam]] B = $(\vec{b_{1}},\dots,\vec{b_{n}})$ tvoří [[Báze|bázi]] [[Lineární prostor nad tělesem F|lineárního prostoru]] L. Pro každý vektor $\vec{x}$ v L existuje jediný seznam $(\vec{a_{1}},\dots,\vec{a_{n}})$ prvků $\mathbb{F}$ tak, že  $\vec{x} = a_{1} \cdot \vec{b_{1}} + \dots +a_{n} \cdot \vec{b_{n}}$. [[Seznam|Seznamu]] $(\vec{a_{1}},\dots,\vec{a_{n}})$ pak říkáme souřadnice vektoru $\vec{x}$ vzhledem k uspořádané bázi B. Značíme:
$$
coord_{B}(\vec{x}) = \begin{pmatrix}
a_{1} \\
\vdots \\
a_{n}
\end{pmatrix}
$$

### Intuitivně
Přeměna souřadnic v jednom prostoru do druhého. Souřadnice je kolikrát daného vektoru z báze potřebuji abych ho složil v prostoru. Např.: když máme bázi B = {(1,0), (0,1)}, souřadnice vektoru (4,5) vzhledem k této bázi budou $coord_{B}(\vec{x}) = \begin{pmatrix}4 \\5\end{pmatrix}$ 

Pro složitější případ: $B = \{ \mathbf{b}_1 = (1,1), \; \mathbf{b}_2 = (1,-1) \}$, a vektor (2,0), souřadnice by pak byly: $coord_{B}(\vec{x}) = \begin{pmatrix}1 \\1\end{pmatrix}$ , protože ke složení tohoto vektoru je potřeba jednou b1 a jednou b2.

Můžeme počítat souřadnice i například po zobrazení vektoru do jiného prostoru.

Nebo souřadnice polynomu když máme uspořádané báze $B = (x^{2},x,1)$ a $C = (x^{2} + x +3, x+3, 1)$ prostoru $\mathbb{R}^{\leq 2}[x]$ kde. Pak souřadnice polynomu $3x^{2} + 2x +5$ vzhledem k bázi C je:
$coord_{C}([x]) = \begin{pmatrix}3 \\-1 \\-1\end{pmatrix}$ 