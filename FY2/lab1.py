import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# ZÁKLADNÍ PARAMETRY
# ==========================================
lambda_red = 635e-9  # Vlnová délka červeného laseru [m]
# lambda_green = 532e-9  # Odkomentuj, pokud budeš dělat i zelený laser

# ==========================================
# 1. OPTICKÁ MŘÍŽKA (zadej svá data)
# ==========================================
l_mrizka = 0.5  # Vzdálenost mřížky od pravítka [m] (UPRAV DLE MĚŘENÍ)

# Řády maxim (m)
m_mrizka = np.array([1, 2, 3])

# Naměřené polohy na pravítku [mm]
x_leva_mrizka = np.array([-15, -31, -48])   # ZADEJ SVOJE HODNOTY (x'_{-m})
x_prava_mrizka = np.array([15, 30, 49])     # ZADEJ SVOJE HODNOTY (x'_{m})

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
l_sterbina = 0.5  # Vzdálenost štěrbiny od senzoru kamery [m] (UPRAV DLE MĚŘENÍ)

# Řády minim (m)
m_sterbina = np.array([1, 2, 3])

# Naměřené polohy minim na senzoru [mm]
x_leva_sterbina = np.array([-5, -10, -15])  # ZADEJ SVOJE HODNOTY
x_prava_sterbina = np.array([5, 10, 15])    # ZADEJ SVOJE HODNOTY

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