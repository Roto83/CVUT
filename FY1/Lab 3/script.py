import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. PARAMETRY APARATURY (z návodu)
# ==========================================
MU_0 = 4 * np.pi * 1e-7  # Magnetická konstanta [N/A^2]
N = 154                  # Počet závitů jedné cívky
A = 0.200                # Poloměr cívek v metrech (200 mm)

# ==========================================
# 2. NAMĚŘENÁ DATA
# ==========================================
# U_data: Urychlovací napětí U [V]
# I_data: Proud Helmholtzovými cívkami I [A]
# L_data: Vzdálenost příčky l v METRECH (dosazuj 0.04, 0.06, 0.08 nebo 0.10)

U_data = np.array([140, 140, 140, 140, 160, 160, 160, 160, 180, 180, 180, 180, 200, 200, 200, 200, 220, 220, 220, 220, 240, 240, 240, 240, 260, 260, 260, 280, 280, 280])  
I_data = np.array([3.030, 1.893, 1.31, 1.07, 3.263, 2.013, 1.48, 1.185 , 3.438, 2.213, 1.62, 1.288, 3.58, 2.348, 1.733, 1.376, 3.8, 2.47, 1.825, 1.451, 3.942, 2.588, 1.91, 1.528, 2.7, 2, 1.6, 2.798, 2.07, 1.662]) 
L_data = np.array([0.04, 0.06, 0.08, 0.10, 0.04, 0.06, 0.08, 0.10, 0.04, 0.06, 0.08, 0.10, 0.04, 0.06, 0.08, 0.10, 0.04, 0.06, 0.08, 0.10, 0.04, 0.06, 0.08, 0.10, 0.06, 0.08, 0.10, 0.06, 0.08, 0.10]) 

# ==========================================
# 3. VÝPOČTY
# ==========================================
# Cyklotronový poloměr Rc = l / 2
R_c = L_data / 2

# Magnetická indukce B v ose cívek
B = (8 / (5 * np.sqrt(5))) * ((MU_0 * N * I_data) / A)

# Výpočet měrného náboje e/me pro každé měření
e_m_calculated = (2 * U_data) / (B**2 * R_c**2)

# Statistika (aritmetický průměr a nejistota typu A)
# Používáme ddof=1 pro výběrovou směrodatnou odchylku
n_measurements = len(e_m_calculated)
e_m_mean = np.mean(e_m_calculated)
e_m_uncertainty = np.std(e_m_calculated, ddof=1) / np.sqrt(n_measurements)

# ==========================================
# 4. VÝPIS DO TERMINÁLU
# ==========================================
print("-" * 65)
print(f"{'VÝSLEDKY PRO JEDNOTLIVÁ MĚŘENÍ (Marian Frýba)':^65}")
print("-" * 65)
print(f"{'Měření':<8} | {'U [V]':<8} | {'I [A]':<8} | {'Rc [m]':<8} | {'e/me [C/kg]':<15}")
print("-" * 65)
for i in range(n_measurements):
    print(f"{i+1:<8} | {U_data[i]:<8.1f} | {I_data[i]:<8.2f} | {R_c[i]:<8.3f} | {e_m_calculated[i]:.4e}")
print("-" * 65)

print("\n" + "-" * 65)
print(f"{'CELKOVÁ STATISTIKA':^65}")
print("-" * 65)
print(f"Počet měření:        {n_measurements}")
print(f"Průměrná hodnota:    {e_m_mean:.4e} C/kg")
print(f"Nejistota typu A:    {e_m_uncertainty:.4e} C/kg")
print(f"Relativní nejistota: {(e_m_uncertainty/e_m_mean)*100:.2f} %")
print("-" * 65)

# ==========================================
# 5. GRAF A LINEÁRNÍ REGRESE (BAREVNĚ PODLE PŘÍČEK)
# ==========================================
# Ze vztahu e/m = 2U / (B*Rc)^2 plyne linearizovaný tvar: 2U = (e/m) * (B*Rc)^2
# Osa y: 2U
# Osa x: (B*Rc)^2

x = (B * R_c)**2
y = 2 * U_data

plt.figure(figsize=(10, 7))

# Nalezení unikátních vzdáleností příček
unique_L = np.unique(L_data)

# Paleta výrazných barev pro jednotlivé příčky
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'] 

# Vykreslení datových bodů rozdělených podle vzdálenosti příčky l
for i, L_val in enumerate(unique_L):
    # Najdeme indexy, kde se L_data rovná aktuální vzdálenosti
    idx = np.where(L_data == L_val)
    
    # Převedeme na cm pro hezčí popisek v legendě
    L_cm = int(round(L_val * 100))
    
    plt.plot(x[idx], y[idx], 'o', color=colors[i % len(colors)], 
             markersize=8, label=f'Naměřeno pro l = {L_cm} cm')

# Výpočet lineární regrese (proložení přímky y = k*x procházející počátkem)
k_fit = np.linalg.lstsq(x[:, np.newaxis], y, rcond=None)[0][0]
x_fitLine = np.linspace(0, max(x) * 1.1, 100)
y_fitLine = k_fit * x_fitLine

# Vykreslení fitu
plt.plot(x_fitLine, y_fitLine, '-', color='black', linewidth=2, zorder=0, 
         label=f'Lineární fit (směrnice e/m = {k_fit:.2e} C/kg)')

# Formátování grafu
plt.title('Určení měrného náboje z lineární závislosti', fontsize=14, pad=15)
plt.xlabel('$(B \cdot R_c)^2$  [$T^2 \cdot m^2$]', fontsize=12)
plt.ylabel('$2U$  [V]', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=11)

# Zobrazení grafu
plt.tight_layout()
plt.show()