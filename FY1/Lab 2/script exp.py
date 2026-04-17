import math
import matplotlib.pyplot as plt

# ==========================================
# Dosazení parametrů
# ==========================================

# Parametry struny
l = 1.0       # Délka struny [m]
d = 0.001     # Průměr struny [m] (např. 1 mm = 0.001)

# Parametry etalonu (válcové desky)
m = 2.5       # Hmotnost desky [kg]
R = 0.1 / 2     # Poloměr desky [m] (dosadit průměř)

# Naměřené časy (doba 1 kyvu)
Tk_deska = 5.24  # Doba kyvu s deskou [s]
Tk_rotor = 4.80  # Doba kyvu s neznámým rotorem [s]


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