import math
import matplotlib.pyplot as plt

# ==========================================
# Dosazení parametrů
# ==========================================

# Parametry struny
l = 0.961       # Délka struny [m]
d_avg = {0.00117, 0.00117, 0.00117, 0.00117, 0.00117, 0.00117, 0.00117, 0.00117, 0.00117, 0.00117}     # Průměr struny [m] (např. 1 mm = 0.001)
d = sum(d_avg) / len(d_avg)

# Parametry etalonu (válcové desky)
m = 5.13       # Hmotnost desky [kg]
R = 0.213 / 2  # Poloměr desky [m] (dosadit průměř)

# Naměřené časy (doba 1 kyvu) (odhadovaná chyba 0,3 s)
# DESKA
# Čas 10 kyvů: 43,1 s
# interval pro 10 kyvů: 42.8s < 10.Tk_deska < 43,4 s
# Čas 20 kyvů: 85,6 s < 20.Tk_deska < 86,8 s //86,6
# interval pro 20 kyvů: 86,3 s < 20.Tk_deska < 86,9 s
# Čas 50 kyvů: 214 s < 50.Tk_deska < 217,25 s //217,2
# interval pro 50 kyvů: 216,9 s < 50.Tk_deska < 217,5 s
# Čas 100 kyvů: 433,8 s < 100.Tk_deska < 435 s //434,4
# interval pro 100 kyvů: 434,1 < 434,4 < 434,7 s
#chyba u(Tk_deska) = (0.003/√3) = 0.00173205 s

# ROTOR
# Čas 10 kyvů: 10,9s
# interval pro 10 kyvů: 10,6s < 10.Tk_rotor < 11,2s 
# Čas 20 kyvů: 21,2 s < 20.Tk_rotor < 22,4 s //22
# interval pro 20 kyvů: 21,7 s < 20.Tk_rotor < 22,3 s
# Čas 50 kyvů: 54,25 s < 50.Tk_rotor < 55,75 s //55,4
# interval pro 50 kyvů: 55,1 s < 50.Tk_rotor < 55,7 s
# Čas 100 kyvů: 110,2 s < 100.Tk_rotor < 111,4 s //111,3
# interval pro 100 kyvů: 111 s < 100.Tk_rotor < 111,6 s
#chyba u(Tk_rotor) = (0.003/√3) = 0.00173205 s

Tk_deska = 4.344  # Doba kyvu s deskou [s]
Tk_rotor = 1.113  # Doba kyvu s neznámým rotorem [s]


# ==========================================
# 2. VÝPOČTY (VNITŘNÍ OBVODY)
# ==========================================

# Moment setrvačnosti desky J = 1/2 * m * R^2
J_deska = 0.5 * m * (R ** 2)

# Modul pružnosti ve smyku G = (32 * pi * l * J_deska) / (d^4 * Tk_deska^2)
G = (32 * math.pi * l * J_deska) / ((d ** 4) * (Tk_deska ** 2))

# Moment setrvačnosti rotoru J_rotor = (G * d^4 * Tk_rotor^2) / (32 * pi * l)
J_rotor = (G * (d ** 4) * (Tk_rotor ** 2)) / (32 * math.pi * l)

# Převod G na GPa pro hezčí zobrazení
G_GPa = G / 1e9


# ==========================================
# 3. VÝPIS
# ==========================================

def print_separator(char="=", length=60):
    print(char * length)

print("\n")
print_separator("█", 60)
print("      LABORATORNÍ ÚLOHA: TORZNÍ KYVADLO MARIAN FRÝBA    ")
print_separator("█", 60)

print("\n[ VSTUPNÍ PARAMETRY ]")
print_separator("-")
print(f"Délka struny (l):          {l:.4f} m")
print(f"Průměr struny (d):         {d:.4f} m  ({d*1000:.1f} mm)")
print(f"Hmotnost desky (m):        {m:.4f} kg")
print(f"Poloměr desky (R):         {R:.4f} m")
print(f"Doba kyvu - deska (Tk1):   {Tk_deska:.4f} s")
print(f"Doba kyvu - rotor (Tk2):   {Tk_rotor:.4f} s")

print("\n[ VÝSLEDNÉ HODNOTY ]")
print_separator("-")
print(f"Moment setrvačnosti desky (J_deska):  {J_deska:.6f} kg*m^2")
print(f"Modul pružnosti ve smyku struny (G):  {G:.2e} Pa")
print(f"                                      {G_GPa:.2f} GPa")
print(f"Moment setrvačnosti rotoru (J_rotor): {J_rotor:.6f} kg*m^2")
print_separator("█", 60)
print("\n")


# ==========================================
# 4. GRAFICKÉ ZOBRAZENÍ (OKNO S GRAFEM)
# ==========================================

labels = ['Etalon (Válcová deska)', 'Neznámý rotor']
values = [J_deska, J_rotor]

# Vykreslení sloupkového grafu
plt.figure(figsize=(8, 5))
# Použití temných barev (Dark Grey a Blood Red)
bars = plt.bar(labels, values, color=['#2b2b2b', '#8b0000'], edgecolor='black', linewidth=1.5)

plt.ylabel('Moment setrvačnosti $J$ [kg$\cdot$m$^2$]', fontsize=12)
plt.title('Porovnání momentů setrvačnosti', fontsize=14, fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Přidání přesných čísel přímo nad sloupce
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + (max(values) * 0.02), 
             f"{yval:.5f}", ha='center', va='bottom', fontweight='bold')

# Vykreslení
plt.tight_layout()
plt.show()