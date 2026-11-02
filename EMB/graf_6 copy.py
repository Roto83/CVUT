import numpy as np
import matplotlib.pyplot as plt

# Naměřená data (Delta R = R_x - 1000)
delta_R = np.array([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500])

# Výstupní napětí v mV pro jednotlivá zapojení
U_MN = np.array([0.127, 60.946, 118.98, 174.22, 226.99, 277.37, 325.64, 371.78, 416.03, 458.48, 499.23])
U_MP = np.array([0.0099, 4.810, 9.484, 14.018, 18.436, 22.724, 26.913, 30.986, 34.954, 38.898, 42.602])
U_LM = np.array([0.130, 62.443, 124.89, 187.25, 249.65, 311.96, 374.40, 436.77, 499.08, 561.39, 623.95])

# KOREKCE: Softwarové přeškálování dat proudového můstku
# Použijeme hodnoty při 50 Ohmech (index 1), abychom srovnali strmost s linearizovaným můstkem.
korekce = U_LM[1] / U_MP[1]
U_MP_korigovane = U_MP * korekce

# --- NOVÁ ČÁST: Výpis hodnot do terminálu ---
print(f"Aplikován korekční faktor: {korekce:.4f}\n")
print("Korigované hodnoty proudového můstku (pro protokol):")
print("Rx [Ω]\t| ΔR [Ω]\t| U_MP (korigováno) [mV]")
print("-" * 55)
for i in range(len(delta_R)):
    Rx = 1000 + delta_R[i]
    print(f"{Rx}\t| {delta_R[i]}\t\t| {U_MP_korigovane[i]:.3f}")
print("-" * 55 + "\n")
# --------------------------------------------

# Výpočet ideální přímky z koncových bodů linearizovaného můstku
# Směrnice k = (U_max - U_min) / (Delta_R_max - Delta_R_min)
k = (U_LM[-1] - U_LM[0]) / (delta_R[-1] - delta_R[0])
U_ideal = k * delta_R + U_LM[0]

# Výpočet odchylek od společné ideální přímky
odchylka_MN = U_MN - U_ideal
odchylka_MP = U_MP_korigovane - U_ideal  # Použita korigovaná data!
odchylka_LM = U_LM - U_ideal

# Vykreslení grafu
plt.figure(figsize=(10, 6))

plt.plot(delta_R, odchylka_MN, marker='o', label='Napěťový můstek (fMN)')
plt.plot(delta_R, odchylka_MP, marker='s', label='Proudový můstek (fMP) - korigováno')
plt.plot(delta_R, odchylka_LM, marker='^', label='Linearizovaný můstek (fLM)')

# Estetika grafu
plt.axhline(0, color='black', linestyle='--', linewidth=1) # Nulová osa (ideální linearita)
plt.title('Odchylky výstupního napětí můstků od lineárního průběhu')
plt.xlabel('Změna odporu $\Delta R$ [$\Omega$]')
plt.ylabel('Odchylka od linearity $\Delta U$ [mV]')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

# Zobrazení
plt.tight_layout()
plt.show()