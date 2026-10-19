import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# 1. ZÁKLADNÍ PARAMETRY A NAMĚŘENÁ DATA
# =====================================================================
lambda_red = 635e-9  # Vlnová délka červeného laseru [m]

# --- MŘÍŽKA 600 štěrbin/mm ---
l_mrizka_600 = 0.25  # Vzdálenost mřížky od pravítka [m]
m_mrizka_600 = np.array([1, 2]) # Řády maxim
x_leva_mrizka_600 = np.array([298, 75]) # Souřadnice levých maxim [mm]
x_prava_mrizka_600 = np.array([525, 764]) # Souřadnice pravých maxim [mm]

# --- MŘÍŽKA 80 štěrbin/mm ---
l_mrizka_80 = 0.6  # Vzdálenost mřížky od pravítka [m]
m_mrizka_80 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # Řády maxim
x_leva_mrizka_80 = np.array([379, 347, 314, 281, 246, 211, 172, 132, 88, 40]) # Souřadnice levých maxim [mm]
x_prava_mrizka_80 = np.array([442, 475, 508, 542, 576, 613, 652, 693, 740, 790])  # Souřadnice pravých maxim [mm]

# --- ŠTĚRBINY (všechny měřeny ve stejné vzdálenosti) ---
l_sterbina = 0.25  # Vzdálenost štěrbin od senzoru kamery [m]

# Štěrbina 0.4 mm
m_sterbina_04 = np.array([1, 2, 3])
x_leva_sterbina_04 = np.array([11.51, 11.02, 10.38]) 
x_prava_sterbina_04 = np.array([12.63, 13.09, 13.62]) 

# Štěrbina 0.2 mm
m_sterbina_02 = np.array([1, 2, 3])
x_leva_sterbina_02 = np.array([10.57, 9.6, 8.64])
x_prava_sterbina_02 = np.array([12.92, 14.01, 14.78])

# Štěrbina 0.1 mm
m_sterbina_01 = np.array([1, 2, 3])
x_leva_sterbina_01 = np.array([9.26, 7.73, 5.38])
x_prava_sterbina_01 = np.array([13.98, 16.63, 18.14])

# =====================================================================
# 2. VÝPOČETNÍ A VYKRESLOVACÍ FUNKCE
# =====================================================================
mereni = [
    {"nazev": "Mřížka 600 štěrbin/mm", "typ": "mrizka", "l": l_mrizka_600, "m": m_mrizka_600, "x_leva": x_leva_mrizka_600, "x_prava": x_prava_mrizka_600, "ocekavane": 1/600e3},
    {"nazev": "Mřížka 80 štěrbin/mm", "typ": "mrizka", "l": l_mrizka_80, "m": m_mrizka_80, "x_leva": x_leva_mrizka_80, "x_prava": x_prava_mrizka_80, "ocekavane": 1/80e3},
    {"nazev": "Štěrbina 0.4 mm", "typ": "sterbina", "l": l_sterbina, "m": m_sterbina_04, "x_leva": x_leva_sterbina_04, "x_prava": x_prava_sterbina_04, "ocekavane": 0.4e-3},
    {"nazev": "Štěrbina 0.2 mm", "typ": "sterbina", "l": l_sterbina, "m": m_sterbina_02, "x_leva": x_leva_sterbina_02, "x_prava": x_prava_sterbina_02, "ocekavane": 0.2e-3},
    {"nazev": "Štěrbina 0.1 mm", "typ": "sterbina", "l": l_sterbina, "m": m_sterbina_01, "x_leva": x_leva_sterbina_01, "x_prava": x_prava_sterbina_01, "ocekavane": 0.1e-3}
]

fig, axs = plt.subplots(2, 3, figsize=(16, 10))
axs = axs.flatten()

print(f"{'Měření':<25} | {'Průměrný výsledek [m]':<22} | {'Odchylka od tabulek [%]':<25}")
print("-" * 75)

for i, data in enumerate(mereni):
    # Výpočet přesné vzdálenosti od středu (x_m) v metrech
    x_avg_m = ((data["x_prava"] - data["x_leva"]) / 2) / 1000
    
    # Výpočet sin(phi)
    sin_phi = x_avg_m / np.sqrt(x_avg_m**2 + data["l"]**2)
    
    # Výpočet mřížkové konstanty d nebo šířky štěrbiny b
    vypoctena_hodnota = (data["m"] * lambda_red) / sin_phi
    prumer = np.mean(vypoctena_hodnota)
    
    # Odchylka
    odchylka = abs(prumer - data["ocekavane"]) / data["ocekavane"] * 100
    
    print(f"{data['nazev']:<25} | {prumer:.4e} m{'':<8} | {odchylka:.2f} %")
    
    # Vykreslení grafu pro dané měření
    x_osa = data["m"] * lambda_red
    y_osa = sin_phi
    
    barva = 'ro' if data["typ"] == "mrizka" else 'bo'
    label_bod = 'Naměřená maxima' if data["typ"] == "mrizka" else 'Naměřená minima'
    oznaceni = 'd' if data["typ"] == "mrizka" else 'b'
    
    axs[i].plot(x_osa, y_osa, barva, label=label_bod)
    
    # Lineární regrese přes počátek (y = k*x)
    k = np.linalg.lstsq(x_osa[:, np.newaxis], y_osa, rcond=None)[0][0]
    axs[i].plot(x_osa, k * x_osa, 'k--', label=f'Fit ({oznaceni} = {1/k:.2e} m)')
    
    axs[i].set_title(data["nazev"])
    axs[i].set_xlabel(r'$m \cdot \lambda$ [m]')
    axs[i].set_ylabel(r'$\sin(\varphi)$ [-]')
    axs[i].legend()
    axs[i].grid(True)

# Skrytí 6. prázdného grafu (máme jich jen 5)
fig.delaxes(axs[5])

plt.tight_layout()
plt.show()