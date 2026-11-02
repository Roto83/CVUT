import numpy as np
import matplotlib.pyplot as plt

# Naměřená data (Delta R = R_x - 1000)
delta_R = np.array([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500])

# Výstupní napětí v mV
U_MN = np.array([0.127, 60.946, 118.98, 174.22, 226.99, 277.37, 325.64, 371.78, 416.03, 458.48, 499.23])
U_MP = np.array([0.129, 61.728, 121.87, 180.52, 237.79, 293.67, 348.34, 401.67, 453.83, 504.82, 554.69])
U_LM = np.array([0.130, 62.443, 124.89, 187.25, 249.65, 311.96, 374.40, 436.77, 499.08, 561.39, 623.95])

# Výpočet ideální přímky z koncových bodů linearizovaného můstku (dle zadání 6.1.6)
# Směrnice k = (U_max - U_min) / (Delta_R_max - Delta_R_min)
k = (U_LM[-1] - U_LM[0]) / (delta_R[-1] - delta_R[0])
U_ideal = k * delta_R + U_LM[0]

# Poznámka: Naměřené hodnoty U_MP jsou zhruba 10x menší než by měly teoreticky být 
# (pravděpodobně byl zdroj proudu nastaven na 0.5 mA místo 5 mA). 
# Pro korektní vizualizaci nelinearity vůči společné přímce by bylo nutné data U_MP vynásobit 10.
# Zde striktně dodržujeme výpočet odchylek z původních dat:
odchylka_MN = U_MN - U_ideal
odchylka_MP = U_MP - U_ideal 
odchylka_LM = U_LM - U_ideal

# Vykreslení grafu
plt.figure(figsize=(10, 6))

plt.plot(delta_R, odchylka_MN, marker='o', label='Napěťový můstek (fMN)')
plt.plot(delta_R, odchylka_MP, marker='s', label='Proudový můstek (fMP)')
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