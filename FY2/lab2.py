import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# 1. ČÁST: PLANCKOVA KONSTANTA A VÝSTUPNÍ PRÁCE
# =====================================================================
# Vlnové délky použitých LED v nm
lambdas_part1 = np.array([472, 505, 525, 588, 611])

# ZADEJ NAMĚŘENÁ BRZDNÁ NAPĚTÍ U_b PRO JEDNOTLIVÉ LED [V]
# Doplň hodnoty ve stejném pořadí jako jsou vlnové délky výše
U_b_part1 = np.array([0.644, 0.482, 0.414, 0.133, 0.082])  # PŘEPIŠ SVÝMI DATY

# Výpočet kmitočtu v PHz (10^15 Hz)
c = 299792458  # rychlost světla [m/s]
f_PHz = (c / (lambdas_part1 * 1e-9)) / 1e15

# Maximální kinetická energie E_k_max v eV se číselně rovná brzdnému napětí U_b ve V
E_k_max = U_b_part1

# Lineární regrese: E_k_max = a1 * f + a0
kolo_fit = np.polyfit(f_PHz, E_k_max, 1)
a1, a0 = kolo_fit[0], kolo_fit[1]

# Výpočet hledaných konstant
h_exp = 1.6022e-34 * a1
A_exp = -a0
f0_exp = A_exp / a1  # Prahový kmitočet v PHz

print("--- 1. PLANCKOVA KONSTANTA A VÝSTUPNÍ PRÁCE ---")
print(f"Rovnice regrese: E_k_max = {a1:.4f} * f + ({a0:.4f})")
print(f"Planckova konstanta h:  {h_exp:.4e} J.s")
print(f"Výstupní práce A:       {A_exp:.4f} eV")
print(f"Prahový kmitočet f_0:   {f0_exp:.4f} PHz\n")

# =====================================================================
# 2. ČÁST: NEZÁVISLOST ENERGIE NA INTENZITĚ SVĚTLA
# =====================================================================
print("--- 2. VLIV INTENZITY NA E_k_max ---")
# ZADEJ NAMĚŘENÁ BRZDNÁ NAPĚTÍ U_b PRO RŮZNÉ INTENZITY [V]
# Pořadí intenzit: 100%, 80%, 60%, 40%, 20%
intenzity_pct = [100, 80, 60, 40, 20]

data_intenzity = {
    472: np.array([0.644, 0.641, 0.637, 0.633, 0.621]), # PŘEPIŠ SVÝMI DATY PRO 472 nm
    525: np.array([0.414, 0.412, 0.408, 0.403, 0.395]), # PŘEPIŠ SVÝMI DATY PRO 525 nm
    611: np.array([0.082, 0.082, 0.082, 0.082, 0.082])  # PŘEPIŠ SVÝMI DATY PRO 611 nm
}

print(f"{'Vlnová délka':<15} | {'Změna E_k_max (20% -> 100%)'}")
print("-" * 45)
for wl, U_b_vals in data_intenzity.items():
    E_k_100 = U_b_vals[0] # hodnota pro 100%
    E_k_20 = U_b_vals[-1] # hodnota pro 20%
    zmena_pct = ((E_k_100 - E_k_20) / E_k_20) * 100
    print(f"{wl} nm{'':<9} | {zmena_pct:+.2f} %")
print("\n")

# =====================================================================
# 3. ČÁST: VOLTAMPÉROVÁ CHARAKTERISTIKA (I_f v závislosti na U_KA)
# =====================================================================
# ZADEJ NAMĚŘENÁ DATA NAPĚTÍ U_KA [V] A FOTOPROUDU I_f [nA]
# Pro každou vlnovou délku zadej pole hodnot U a odpovídající pole I.
va_charakteristiky = {
    472: {
        "U": np.array([0.0, 0.06, 0.12, 0.18, 0.24, 0.3, 0.36, 0.42, 0.48, 0.54, 0.598]),     # PŘEPIŠ SVÝMI DATY
        "I": np.array([1.984, 1.67, 1.376, 1.107, 0.852, 0.625, 0.431, 0.268, 0.143, 0.055, 0]) # PŘEPIŠ SVÝMI DATY
    },
    505: {
        "U": np.array([0.0, 0.06, 0.12, 0.18, 0.24, 0.3, 0.36, 0.42, 0.458]),          # PŘEPIŠ SVÝMI DATY
        "I": np.array([1.995, 1.633, 1.303, 0.994, 0.709, 0.46, 0.248, 0.081, 0])       # PŘEPIŠ SVÝMI DATY
    },
    525: {
        "U": np.array([0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.404]),               # PŘEPIŠ SVÝMI DATY
        "I": np.array([1.999, 1.673, 1.382, 1.105, 0.837, 0.593, 0.368, 0.173, 0.012, 0])             # PŘEPIŠ SVÝMI DATY
    }
}

# =====================================================================
# VYKRESLENÍ GRAFŮ
# =====================================================================
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Graf 1: Závislost maximální kinetické energie na kmitočtu
axs[0].plot(f_PHz, E_k_max, 'bo', label='Naměřené hodnoty')
f_lin = np.linspace(min(f_PHz)-0.05, max(f_PHz)+0.05, 100)
axs[0].plot(f_lin, a1 * f_lin + a0, 'k--', label=f'Fit (A = {A_exp:.2f} eV)')

axs[0].axhline(0, color='black', linewidth=0.8)
axs[0].axvline(f0_exp, color='red', linestyle=':', label=f'Prahový kmitočet f_0 = {f0_exp:.3f} PHz')

axs[0].set_title('Závislost max. kinetické energie na kmitočtu')
axs[0].set_xlabel('Kmitočet $f$ [PHz]')
axs[0].set_ylabel('Max. kinetická energie $E_{k~max}$ [eV]')
axs[0].legend()
axs[0].grid(True)

# Graf 2: Voltampérové charakteristiky
barvy = {472: 'b', 505: 'g', 525: 'r'}
for wl, data in va_charakteristiky.items():
    U = data["U"]
    I = data["I"]
    
    # Body
    axs[1].plot(U, I, marker='o', linestyle='', color=barvy[wl], label=f'{wl} nm (data)')
    
    # Polynom 3. stupně pro proložení
    poly_fit = np.polyfit(U, I, 3)
    p3 = np.poly1d(poly_fit)
    U_lin = np.linspace(min(U), max(U), 100)
    
    axs[1].plot(U_lin, p3(U_lin), color=barvy[wl], linestyle='-', alpha=0.7, label=f'{wl} nm (fit 3. st.)')

axs[1].set_title('Závislost fotoproudu na brzdném napětí')
axs[1].set_xlabel('Napětí $U_{KA}$ [V]')
axs[1].set_ylabel('Fotoproud $I_f$ [nA]')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()