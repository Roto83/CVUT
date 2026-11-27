import matplotlib.pyplot as plt
import numpy as np

# Naměřená a vypočtená data z tabulky
U_in = np.array([6, 61, 1003, 2503, 5008, 7507, 9006, 9904])  # [mV]
delta_U = np.array([-6, -22, -26, -3, -8, -7, -21, -18])      # [mV]

# Teoretický kvantovací krok (1 LSB = 10 000 mV / 256)
LSB = 10000 / 256  # 39.0625 mV

# Výpočet teoretické pilovité kvantovací chyby (truncating ADC: 0 až -1 LSB)
u_teor = np.linspace(0, 10000, 10000)
n_teor = np.floor(u_teor / LSB)
delta_u_teor = n_teor * LSB - u_teor

plt.figure(figsize=(10, 5.2))

# 1. Teoretická pilovitá kvantovací chyba na pozadí
plt.plot(u_teor, delta_u_teor, color='gray', alpha=0.35, linewidth=0.8, 
         label='Teoretická kvantovací chyba (pilovitý průběh 0 až $-1$ LSB)')

# 2. Referenční vodorovné čáry (0 LSB a -1 LSB)
plt.axhline(0, color='black', linestyle='-', linewidth=1)
plt.axhline(-LSB, color='red', linestyle='--', linewidth=1, label=f'$-1$ LSB ({-LSB:.2f} mV)')

# 3. Svislé tečkované čáry od nuly k bodům + samotné body
plt.vlines(U_in, ymin=delta_U, ymax=0, color='#1f77b4', linestyle=':', linewidth=1.5)
plt.scatter(U_in, delta_U, color='#1f77b4', s=55, zorder=5, 
            label='Naměřená odchylka $\Delta U = U_{ADC} - U_{IN}$')

# Popisky a formátování
plt.title('Odchylky převodní charakteristiky 8bitového A/D převodníku', fontsize=12, pad=12)
plt.xlabel('Vstupní napětí $U_{IN}$ [mV]', fontsize=11)
plt.ylabel('Odchylka $\Delta U$ [mV]', fontsize=11)

plt.xlim(-250, 10250)
plt.ylim(-45, 8)

# Mřížka přesně přes 1/4, 1/2 a 3/4 rozsahu
plt.xticks(np.arange(0, 10001, 2500))

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='lower right', framealpha=0.95)

plt.tight_layout()
plt.savefig('odchylky_adc_sawtooth.png', dpi=300)
plt.show()