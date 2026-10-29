import numpy as np
import matplotlib.pyplot as plt

n = 1.0        # počet molů ideálního plynu
R = 8.314      # univerzální plynová konstanta [J/(mol*K)]
gamma = 1.4    # Poissonova konstanta (dvouatomový plyn)

# Teploty ohřívače (T_H) a chladiče (T_C) [K]
T_H = 600.0
T_C = 300.0

# Počáteční objemy (stav 1 a stav 2) pro první izotermu [m^3]
V1 = 0.01
V2 = 0.025

# Dopočet stavů 3 a 4 pomocí rovnic pro adiabatu
V3 = V2 * (T_H / T_C)**(1 / (gamma - 1))
V4 = V1 * (T_H / T_C)**(1 / (gamma - 1))

# Tlaky v uzlových bodech z rovnice ideálního plynu pV = nRT
P1 = n * R * T_H / V1
P2 = n * R * T_H / V2
P3 = n * R * T_C / V3
P4 = n * R * T_C / V4

# Data pro křivky
# 1 -> 2: Izotermická expanze
v12 = np.linspace(V1, V2, 100)
p12 = n * R * T_H / v12             

# 2 -> 3: Adiabatická expanze
v23 = np.linspace(V2, V3, 100)
p23 = P2 * (V2 / v23)**gamma        

# 3 -> 4: Izotermická komprese
v34 = np.linspace(V3, V4, 100)
p34 = n * R * T_C / v34             

# 4 -> 1: Adiabatická komprese
v41 = np.linspace(V4, V1, 100)
p41 = P4 * (V4 / v41)**gamma        

# Vykreslení grafu
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(v12, p12, 'r-', linewidth=2.5, label=f'1-2: Izotermická expanze ($T_H$ = {T_H} K)')
ax.plot(v23, p23, 'r--', linewidth=2.5, label='2-3: Adiabatická expanze')
ax.plot(v34, p34, 'b-', linewidth=2.5, label=f'3-4: Izotermická komprese ($T_C$ = {T_C} K)')
ax.plot(v41, p41, 'b--', linewidth=2.5, label='4-1: Adiabatická komprese')

# Výplň plochy (vykonaná práce)
ax.fill(np.concatenate([v12, v23, v34, v41]),
        np.concatenate([p12, p23, p34, p41]),
        color='gray', alpha=0.15, label='Vykonaná práce ($W$)')

# Body
V_points = [V1, V2, V3, V4]
P_points = [P1, P2, P3, P4]
ax.scatter(V_points, P_points, color='black', zorder=5)

ax.text(V1, P1, '  1', fontsize=12, va='bottom', fontweight='bold')
ax.text(V2, P2, '  2', fontsize=12, va='bottom', fontweight='bold')
ax.text(V3, P3, '  3', fontsize=12, va='top', fontweight='bold')
ax.text(V4, P4, '4  ', fontsize=12, va='top', ha='right', fontweight='bold')

# Hodnoty pro jednotlivé body
info_text = (
    "Hodnoty v uzlových bodech:\n"
    f"Bod 1: $T$ = {T_H} K,  $V$ = {V1:.3f} m$^3$,  $p$ = {P1/1000:.1f} kPa\n"
    f"Bod 2: $T$ = {T_H} K,  $V$ = {V2:.3f} m$^3$,  $p$ = {P2/1000:.1f} kPa\n"
    f"Bod 3: $T$ = {T_C} K,  $V$ = {V3:.3f} m$^3$,  $p$ = {P3/1000:.1f} kPa\n"
    f"Bod 4: $T$ = {T_C} K,  $V$ = {V4:.3f} m$^3$,  $p$ = {P4/1000:.1f} kPa"
)

# Nastavení vzhledu
bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="gray", alpha=0.9)

# Umístění boxu
ax.text(0.5, 0.95, info_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='center',
        bbox=bbox_props, family='monospace')

# Osy
ax.set_title('p-V diagram Carnotova cyklu', fontsize=14, pad=15)
ax.set_xlabel('Objem $V$ [m$^3$]', fontsize=12)
ax.set_ylabel('Tlak $p$ [Pa]', fontsize=12)
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(loc='center right', framealpha=0.9)

plt.tight_layout()
plt.show()