import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# ZÁKLADNÍ PARAMETRY
# ==========================================
lambda_red = 635e-9  # Vlnová délka červeného laseru [m]

# ==========================================
# 1. OPTICKÁ MŘÍŽKA (zadej svá data)
# ==========================================
#l_mrizka = 0.6  # Vzdálenost mřížky od pravítka [m] 80
l_mrizka = 0.25  # Vzdálenost mřížky od pravítka [m] 600 

# Řády maxim (m)
m_mrizka = np.array([1, 2, 3])

# Naměřené polohy na pravítku [mm] pro 80
#x_leva_mrizka = np.array([-37.9, -34.7, -31.4,-28.1, -24.6, -21.1, -17.2, -13.2, -8.8, -4])   # ZADEJ SVOJE HODNOTY (x'_{-m})
#x_prava_mrizka = np.array([44.2, 47.5, 50.8, 54.2, 57.6, 61.3, 65.2, 69.3, 74, 79])     # ZADEJ SVOJE HODNOTY (x'_{m})

# Naměřené polohy na pravítku [mm] pro 600
x_leva_mrizka = np.array([-29.8, -7.5]) 
x_prava_mrizka = np.array([52.5, 76.4]) 

# --- Výpočet pro mřížku ---
x_avg_m = ((x_prava_mrizka - x_leva_mrizka) / 2) / 1000  # Průměr vzdáleností převedený na metry
sin_phi_mrizka = x_avg_m / np.sqrt(x_avg_m**2 + l_mrizka**2)
d_vypocet = (m_mrizka * lambda_red) / sin_phi_mrizka

print("--- OPTICKÁ MŘÍŽKA ---")
print(f"Vypočítané mřížkové konstanty d [m]: {d_vypocet}")
print(f"Průměrné d: {np.mean(d_vypocet):.2e} m")

# ==========================================
# 2. ŠTĚRBINA (zadej svá data)
# ==========================================
l_sterbina = 0.25  # Vzdálenost štěrbiny od senzoru kamery [m] (UPRAV DLE MĚŘENÍ)

# Řády minim (m)
m_sterbina = np.array([1, 2, 3])

# Naměřené polohy minim na senzoru [mm] 0.4 mm slit peak 12,06mm
x_leva_sterbina = np.array([-11.51, -11.02, -10.38]) 
x_prava_sterbina = np.array([12.63, 13.09, 13.62]) 

# Naměřené polohy minim na senzoru [mm] 0.2 mm slit peak 11,9mm
x_leva_sterbina = np.array([-10.57, -9.6, -8.64])
x_prava_sterbina = np.array([12.92, 14.01, 14.78])

# Naměřené polohy minim na senzoru [mm] 0.1 mm slit peak 11,91mm
x_leva_sterbina = np.array([-9.26, -7.73, -5.38])
x_prava_sterbina = np.array([13.98, 16.63, 18.14])

# --- Výpočet pro štěrbinu ---
x_avg_s = ((x_prava_sterbina - x_leva_sterbina) / 2) / 1000  # Průměr vzdáleností převedený na metry
sin_phi_sterbina = x_avg_s / np.sqrt(x_avg_s**2 + l_sterbina**2)
b_vypocet = (m_sterbina * lambda_red) / sin_phi_sterbina

print("\n--- ŠTĚRBINA ---")
print(f"Vypočítané šířky štěrbiny b [m]: {b_vypocet}")
print(f"Průměrné b: {np.mean(b_vypocet):.2e} m")

# ==========================================
# VYKRESLENÍ GRAFŮ
# ==========================================
plt.figure(figsize=(12, 5))

# --- Graf pro mřížku ---
plt.subplot(1, 2, 1)
x_osa_m = m_mrizka * lambda_red
y_osa_m = sin_phi_mrizka

plt.plot(x_osa_m, y_osa_m, 'ro', label='Naměřená maxima')
# Lineární regrese (fit přes nulu y = k*x)
k_m = np.linalg.lstsq(x_osa_m[:, np.newaxis], y_osa_m, rcond=None)[0][0]
plt.plot(x_osa_m, k_m * x_osa_m, 'k--', label=f'Fit (d = {1/k_m:.2e} m)')

plt.title("Ověření ohybu na optické mřížce")
plt.xlabel(r'$m \cdot \lambda$ [m]')
plt.ylabel(r'$\sin(\varphi)$ [-]')
plt.legend()
plt.grid(True)

# --- Graf pro štěrbinu ---
plt.subplot(1, 2, 2)
x_osa_s = m_sterbina * lambda_red
y_osa_s = sin_phi_sterbina

plt.plot(x_osa_s, y_osa_s, 'bo', label='Naměřená minima')
# Lineární regrese (fit přes nulu y = k*x)
k_s = np.linalg.lstsq(x_osa_s[:, np.newaxis], y_osa_s, rcond=None)[0][0]
plt.plot(x_osa_s, k_s * x_osa_s, 'k--', label=f'Fit (b = {1/k_s:.2e} m)')

plt.title("Ověření ohybu na štěrbině")
plt.xlabel(r'$m \cdot \lambda$ [m]')
plt.ylabel(r'$\sin(\varphi)$ [-]')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()