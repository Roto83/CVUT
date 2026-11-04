import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# 1. NASTAVENÍ NEJISTOT APARATURY
# =====================================================================
L0 = 600.0    # Počáteční upínací délka vzorku [mm]
u_L0 = 1.0    # Nejistota počáteční délky [mm] (zadáno v návodu)

# =====================================================================
# 2. NAČTENÍ DAT A VÝPOČTY
# =====================================================================
nazev_souboru = 'namerena_data_roztaznost.xlsx'
xls = pd.ExcelFile(nazev_souboru)

vysledky = []
# Nastavení rozložení okna: nahoře graf (poměr výšky 3), dole tabulka (poměr 1)
fig, (ax_graf, ax_tab) = plt.subplots(2, 1, figsize=(10, 10), gridspec_kw={'height_ratios': [3, 1]})
barvy = ['b', 'r', 'g', 'm', 'c']

for i, sheet_name in enumerate(xls.sheet_names):
    # Načtení dat z konkrétního listu
    df = pd.read_excel(xls, sheet_name)
    t = df.iloc[:, 0].values     # Teplota v °C
    l_hod = df.iloc[:, 1].values # Údaj na hodinkách v mm
    
    # Změna vůči prvnímu (počátečnímu) bodu měření
    dt = t - t[0]
    dl = l_hod - l_hod[0]
    
    # Lineární fit pomocí nejmenších čtverců (získání směrnice A a její nejistoty)
    p, cov = np.polyfit(dt, dl, 1, cov=True)
    A = p[0]                   # Směrnice přímky [mm/°C]
    u_A = np.sqrt(cov[0, 0])   # Standardní nejistota směrnice (z vertikálních odchylek)
    
    # Teoreticky ideální hodnoty prodloužení na fitované přímce pro dané teploty
    dl_ideal = np.polyval(p, dt)
    
    # Výpočet teplotního součinitele délkové roztažnosti (alfa = A / L0)
    alfa = A / L0
    
    # Výpočet celkové nejistoty pro alfa (kombinace chyby směrnice a chyby délky L0)
    rel_u_A = u_A / A
    rel_u_L0 = u_L0 / L0
    u_alfa = alfa * np.sqrt(rel_u_A**2 + rel_u_L0**2)
    
    # Uložení do tabulky
    vysledky.append([sheet_name, f"{alfa:.2e}", f"{u_alfa:.2e}", f"{A:.4e}"])
    
    # --- Vykreslení do grafu ---
    barva = barvy[i%len(barvy)]
    
    # 1. Naměřené datové body
    ax_graf.plot(dt, dl, 'o', color=barva, label=f'{sheet_name} (naměřeno)')
    
    # 2. Ideální regresní přímka
    dt_fit = np.linspace(0, max(dt), 100)
    dl_fit = np.polyval(p, dt_fit)
    ax_graf.plot(dt_fit, dl_fit, '--', color=barva, label=f'{sheet_name} (ideální závislost)')
    
    # 3. Vizualizace vertikálních odchylek (reziduí) od ideální přímky
    # Label přidáme jen pro první bod série, aby se neduplikoval v legendě
    ax_graf.vlines(dt, dl_ideal, dl, colors=barva, linestyles='dotted', alpha=0.7, 
                   label=f'{sheet_name} (vertikální odchylka)' if i == 0 else "")

# =====================================================================
# 3. FORMÁTOVÁNÍ GRAFU A TABULKY PRO VÝSTUP
# =====================================================================
ax_graf.set_title('Závislost prodloužení na změně teploty', fontsize=14)
ax_graf.set_xlabel(r'Změna teploty $\Delta t$ [°C]', fontsize=12)
ax_graf.set_ylabel(r'Prodloužení $\Delta l$ [mm]', fontsize=12)
ax_graf.legend(loc='upper left')
ax_graf.grid(True, linestyle=':', alpha=0.7)

# Vykreslení tabulky místo spodního grafu
ax_tab.axis('tight')
ax_tab.axis('off')
sloupce = ['Vzorek', r'$\alpha$ [°C$^{-1}$]', r'Nejistota $u(\alpha)$ [°C$^{-1}$]', 'Směrnice $A$ [mm/°C]']

tabulka = ax_tab.table(cellText=vysledky, colLabels=sloupce, loc='center', cellLoc='center')
tabulka.auto_set_font_size(False)
tabulka.set_fontsize(12)
tabulka.scale(1, 1.8) # Roztáhnutí buněk

# Úprava hlavičky tabulky
for (row, col), cell in tabulka.get_celld().items():
    if row == 0:
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor('#40466e')
    else:
        cell.set_facecolor('#f4f4f4')

plt.tight_layout()
plt.show()