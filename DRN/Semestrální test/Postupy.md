1. Řešení ODR separací proměnných (první týdny)
	- Za $y'$ dosadit $\frac{dy}{dx}$, (když dělím y tak nesmí být nula a vytvoří se dvě cesty y = 0, y != 0)
	- Trikem upravit do integrálu a zintegrovat (nezapomenout kosntantu)
	- Upravit do tvaru y = ... (Pokud absolutní hodnota tak se ji zbavím $\cdot\pm1$, )
	- (Něco prohlásím jako novou konstantu pokud je potřeba, nesmí se rovnat nule)
	- Spojit se stacionární cestou y = 0 a zapsat obecné řešení
	- Pro partikulární dosadím, určím konstantu a tu dám zpátky
2. Řešení homogenní lineární ODR. (týden 5)
	- Dosadí se za $y=\lambda$ a stupeň derivace se změní na mocninu
	- Určí se nulové body pro $\lambda$
		- Když vyjdou komplexní čísla typu a+bi napíše se to $\alpha e^{ax} \cos(bx)+\beta e^{ax} \sin(bx)$
	- Nulové body se dosadí do $e^{ \lambda x }$. Pokud je tam nulový bod víckrát udělá se víc $e^{ \lambda x }$ každý s navyšujícím se stupněm x (eg. $e^{ \lambda x }$ $xe^{ \lambda x }$ $x^{2}e^{ \lambda x }$...)
	- Ke každému se přidá násobení proměnnou (např. a-z)
	- Sestaví se obecné řešení ($ae^{ \lambda x }$ + $be^{ \lambda x }$...)
	- Asymptotický růst se určuje tím co roste nejrychleji
	- Počáteční podmínky dosadit a vyjde soustava rovnic
3. Odhad tvaru řešení pro nehomogenni lineární ODR. (týden 6)
	- První část jak to předtím s lambadama a získám nulové body z levé strany
	- Určím si kontrolní číslo z = a + bi (a je násobnost exponentu e a b je stupeň v cos/sin)
	- Zkontroluju jestli s nějakými čísly nastává rezonance (jsou stejné, pro rezonanci cos/sin by musely vyjít komplexní čísla) pokud nastane vynásobím to x (případně x nějakého stupně)
	- Pro polynom dosadím obecný polynom $Ax^{2}+Bx+C$
	- Pro exponenciálu dosadím do $Ae^{x}$
	- Pro cos/sin dosadím $A\cos(x)+B\sin(x)$
4. Řešení homogenní soustavy lineárních ODR. (týden 9)
	- Převede se do matice
	- Přidám -$\lambda$ na hlavní diagonále
	- Spočítám determinant
	- Z toho vezmu kořeny
	- Každý kořen zvlášť dosadím zpátky do matice
	- Matici vynásobím vektorem a najdu jeho hodnoty pokud by se to rovnalo nule
	- Vektor vynásobím $e^{xy}$ kde y je ten kořen
	- Tyto vektory pak vynásobím $a$ a $b$ 
	- Vzniknou dvě rovnice jako výsledek