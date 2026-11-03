import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# 1. NASTAVENÍ NEJISTOT MĚŘIDEL A APARATURY
# =====================================================================
# Tyto hodnoty uprav podle toho, jaké rozlišení mají přístroje v laborce
u_t = 1.0     # Odhadovaná nejistota odečtu teploměru [°C]
u_l = 0.01    # Rozlišení/nejistota indikátorových hodinek [mm]

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
    
    # Kód si sám spočítá změnu vůči prvnímu (počátečnímu) bodu měření
    dt = t - t[0]
    dl = l_hod - l_hod[0]
    
    # Lineární fit pomocí nejmenších čtverců (získání směrnice A a její kovarianční matice)
    p, cov = np.polyfit(dt, dl, 1, cov=True)
    A = p[0]                   # Směrnice přímky [mm/°C]
    u_A = np.sqrt(cov[0, 0])   # Standardní nejistota směrnice z fitu
    
    # Výpočet teplotního součinitele délkové roztažnosti (alfa = A / L0)
    alfa = A / L0
    
    # Výpočet kombinované standardní nejistoty pro alfa (zákon šíření nejistot)
    rel_u_A = u_A / A
    rel_u_L0 = u_L0 / L0
    u_alfa = alfa * np.sqrt(rel_u_A**2 + rel_u_L0**2)
    
    # Uložení do tabulky (formátování na vědecký zápis pro alfa)
    vysledky.append([sheet_name, f"{alfa:.2e}", f"{u_alfa:.2e}", f"{A:.4e}"])
    
    # --- Vykreslení do grafu ---
    # Datové body s chybovými kříži (error bars)
    ax_graf.errorbar(dt, dl, xerr=u_t, yerr=u_l, fmt='o', color=barvy[i%len(barvy)], 
                     label=f'{sheet_name} (naměřeno)', capsize=3, alpha=0.8)
    
    # Regresní přímka
    dt_fit = np.linspace(0, max(dt), 100)
    dl_fit = np.polyval(p, dt_fit)
    ax_graf.plot(dt_fit, dl_fit, '--', color=barvy[i%len(barvy)], label=f'{sheet_name} (fit)')

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
tabulka.scale(1, 1.8) # Roztáhnutí buněk, aby to na fotce bylo čitelné

# Úprava hlavičky tabulky (tučné písmo, barva)
for (row, col), cell in tabulka.get_celld().items():
    if row == 0:
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor('#40466e')
    else:
        cell.set_facecolor('#f4f4f4')

plt.tight_layout()
plt.show()