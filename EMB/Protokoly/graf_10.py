import matplotlib.pyplot as plt
import numpy as np

# Naměřená a vypočtená data z tabulky
U_in = np.array([6, 61, 1003, 2503, 5008, 7507, 9006, 9904])  # [mV]
delta_U = np.array([-6, -22, -26, -3, -8, -7, -22, -18])      # [mV]

# Teoretický kvantovací krok (1 LSB = 10 000 mV / 256)
LSB = 10000 / 256  # 39.0625 mV

plt.figure(figsize=(9, 5))

# Vykreslení naměřených odchylek
plt.plot(U_in, delta_U, marker='o', linestyle='-', color='#1f77b4', 
         linewidth=1.5, markersize=7, label='Naměřená odchylka $\Delta U = U_{ADC} - U_{IN}$')

# Vyznačení teoretického pásma pro převodník bez posunu (0 až -1 LSB)
plt.axhspan(-LSB, 0, color='gray', alpha=0.15, label='Teoretické pásmo chyby (0 až $-1$ LSB)')
plt.axhline(0, color='black', linestyle='-', linewidth=0.9)
plt.axhline(-LSB, color='red', linestyle='--', linewidth=1, label=f'$-1$ LSB ({-LSB:.2f} mV)')
plt.axhline(-LSB / 2, color='green', linestyle=':', linewidth=1, label=f'$-0,5$ LSB ({-LSB/2:.2f} mV)')

# Popisky a formátování
plt.title('Závislost odchylky převodní charakteristiky A/D převodníku na vstupním napětí', fontsize=12, pad=12)
plt.xlabel('Vstupní napětí $U_{IN}$ [mV]', fontsize=11)
plt.ylabel('Odchylka $\Delta U$ [mV]', fontsize=11)

plt.xlim(-200, 10200)
plt.ylim(-45, 10)
# Mřížka přesně po čtvrtinách rozsahu (0, 2500, 5000, 7500, 10000 mV)
plt.xticks(np.arange(0, 10001, 2500))
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='lower right', framealpha=0.95)

plt.tight_layout()
# Uložení ve vysokém rozlišení do protokolu
plt.savefig('odchylky_adc.png', dpi=300)
plt.show()