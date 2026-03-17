Za předpokladu, že uvažujeme pouze konzervativní síly, pak Lagrangeovy rovnice II. druhu jsou ve tvaru:$$\frac{d}{dt}\left(  \frac{\partial L}{\partial \dot{q}_{i}} \right)-\frac{\partial L}{\partial q_{i}}=0,\space \forall i=1,\dots,s$$

kde:
- ﻿﻿$q_{i}$ je i-tá zobecněná souřadnice
- ﻿﻿$\dot{q}_{i}$ je i-tá zobecněná rychlost
- ﻿﻿L = T - U je Lagrangeova funkce (lagrangián) s proměnnými $\dot{q}_{i}$, $q_{i}$, t.
- ﻿﻿s je počet stupňů volnosti

→ Soustava tolika obyčejných diferenciálních rovnic 2. řádu, kolik mám stupňů volnosti

Kuchařka:
1) Zjistěte, kolik má systém holonomních vazeb a tím i kolik má stupňů volnosti.
2) Zaveďte zobecněné souřadnice.
3) Napište vztah mezi kartézskými a zobecněnými souřadnicemi.
4) Vyjádřete kinetickou energii (v kartézských a pak v zobecněných).
5) Vyjádřete potenciální energii (v kartézských a pak v zobecněných).
6) Připravte si potřebné derivace.
7) Sestavte Lagrangeovy rovnice II. druhu.
8) Řešte je (když to rozumně jde).

https://reseneulohy.cz/634/vozik-s-kyvadlem

# Zákon zachování v analytické mechanice
Zobecněnou hybnost definujeme jako derivaci Lagrangeovy funkce podle zobecněné rychlosti:
$$p_{i}\equiv  \frac{\partial L}{\partial \dot{q}}$$Obvyklé připomínky:
- ﻿﻿Může se jednat o hybnost v newtonovském slova smyslu, ale nemusí.
- ﻿﻿K i-té zobecněné souřadnici patří i-tá zobecněná hybnost.

Příklady: pojďme dostat zobecněné hybnosti pro
- ﻿﻿vrhy
- ﻿﻿matematické kyvadlo


Zobecněná souřadnice, na které lagrangián explicitně nezávisí (ale na odpovídající zobecněné rychlosti ano), se nazývá cyklická.

Příklad: pohyb hmotného bodu v homogenním gravitačním poli (vrhy):
$$L=\frac{1}{2}m(\dot{x}^{2}+\dot{y}^{2}+\dot{z}^{2})-mgz$$
→ souřadnice x, y jsou cyklické.

Varování: Pojmenování cyklická souřadnice je spíš historické než intuitivní. Vztahuje se na rotační systémy se zachováním momentu hybnosti (např. lagrangián pohybu planety). Občas se používá i „ignorable coordinate".