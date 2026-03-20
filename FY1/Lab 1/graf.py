import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# --- TVOJE NAMĚŘENÁ DATA Z LABORATOŘE ---
# ==========================================

# 1. ČÁST: Hledání průsečíku (měření pro 100 kyvů)
#Marian Frýba
poloha_cocky = np.array([0, 1, 2, 3, 4, 5, 5.25, 5.5]) # Otáčky nebo milimetry

cas_100_dole = np.array([77.401, 77.442, 77.514, 77.562, 77.604, 77.652, 77.661, 77.678]) 
cas_100_nahore = np.array([76.283, 76.723, 76.767, 76.834, 77.113, 77.508, 77.695, 77.762])

# 2. ČÁST: Finální výpočet (měření v nalezeném průsečíku)
cas_500_dole_fin = 388.343
cas_500_nahore_fin = 388.569

L_vzdalenost = 0.596 
nejistota_L = 0.001 
nejistota_citace = 0.001 


# ==========================================
# --- ZPRACOVÁNÍ A VÝPOČTY ---
# ==========================================

tau_dole = cas_100_dole / 100
tau_nahore = cas_100_nahore / 100

rozdil = tau_dole - tau_nahore
idx = np.where(np.diff(np.sign(rozdil)))[0]

cas_500_prumer = (cas_500_dole_fin + cas_500_nahore_fin) / 2
tau_0 = cas_500_prumer / 500
chyba_tau_0 = nejistota_citace / 500

g = (np.pi**2 * L_vzdalenost) / (tau_0**2)

relativni_chyba_L = nejistota_L / L_vzdalenost
relativni_chyba_tau = 2 * (chyba_tau_0 / tau_0)
celkova_nejistota_g = g * np.sqrt(relativni_chyba_L**2 + relativni_chyba_tau**2)

print("=== VÝSLEDKY FINÁLNÍHO MĚŘENÍ ===")
print(f"Redukovaná délka L: {L_vzdalenost:.4f} ± {nejistota_L:.4f} m")
print(f"Doba 1 kyvu (z 500): {tau_0:.5f} ± {chyba_tau_0:.5f} s")
print(f"Vypočtené tíhové zrychlení g: {g:.4f} ± {celkova_nejistota_g:.4f} m/s^2")
print("=================================\n")

# --- Vykreslení grafu ---
plt.figure(figsize=(10, 6))
plt.plot(poloha_cocky, tau_dole, 'o-', label=r'Čočka dole ($\tau_{0d}$)', color='blue')
plt.plot(poloha_cocky, tau_nahore, 's-', label=r'Čočka nahoře ($\tau_{0h}$)', color='red')

if len(idx) > 0:
    i = idx[0]
    x1, x2 = poloha_cocky[i], poloha_cocky[i+1]
    y1_d, y2_d = tau_dole[i], tau_dole[i+1]
    y1_n, y2_n = tau_nahore[i], tau_nahore[i+1]
    
    x_prusecik = x1 + (x2 - x1) * (y1_n - y1_d) / ((y2_d - y1_d) - (y2_n - y1_n))
    y_prusecik = y1_d + (x_prusecik - x1) * (y2_d - y1_d) / (x2 - x1)
    
    # Úprava zde: přidání y_prusecik do popisku a vykreslení obou vodících linek
    plt.plot(x_prusecik, y_prusecik, 'k*', markersize=12, 
             label=f'Průsečík:\nx={x_prusecik:.2f} (poloha)\ny={y_prusecik:.5f} s (doba)')
    
    plt.axvline(x=x_prusecik, color='grey', linestyle='--', alpha=0.7)
    plt.axhline(y=y_prusecik, color='grey', linestyle='--', alpha=0.7)

plt.title('Závislost doby kyvu na poloze čočky')
plt.xlabel('Poloha čočky [otáčky / mm]')
plt.ylabel(r'Doba kyvu $\tau_0$ [s]')
plt.legend()
plt.grid(True)
plt.show()