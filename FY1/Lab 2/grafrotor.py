import matplotlib.pyplot as plt

# ==========================================
# 1. VSTUPNÍ DATA Z MĚŘENÍ
# ==========================================

N_kmity = [10, 20, 50, 100]

# ZDE DOSAĎ SVÉ NAMĚŘENÉ CELKOVÉ ČASY PRO DANÝ POČET KMITŮ [s]
# Příklad: pro 10 kmitů jste naměřili 52.4 s, pro 20 kmitů 104.8 s atd.
casy_mereni = [10.9, 22, 55.4, 111.3] 

# Odhadnutá absolutní chyba měření celkového času (stopky + reakční doba) [s]
chyba_stopek = 0.3 

# ==========================================
# 2. VÝPOČTY (Ořezání šumu)
# ==========================================

# Výpočet doby jednoho kyvu (Tk) pro každý krok
Tk_hodnoty = [t / n for t, n in zip(casy_mereni, N_kmity)]

# Výpočet zmenšující se chyby (meze) pro jeden kyv
Tk_chyby = [chyba_stopek / n for n in N_kmity]

# ==========================================
# 3. TEXTOVÝ VÝPIS DO KONZOLE
# ==========================================
print("\nVývoj přesnosti omezovací metody:")
print("-" * 50)
print(f"{'Počet kmitů (N)':<20} | {'Doba kyvu Tk [s]':<20} | {'Chyba +- [s]':<20}")
print("-" * 50)
for n, tk, err in zip(N_kmity, Tk_hodnoty, Tk_chyby):
    print(f"{n:<20} | {tk:<20.4f} | {err:<20.4f}")
print("-" * 50 + "\n")

# ==========================================
# 4. VYKRESLENÍ GRAFU
# ==========================================

plt.figure(figsize=(9, 6))

# Vykreslení bodů s chybovými úsečkami (error bars)
# Používáme temně červenou ('#8b0000') pro zvýraznění měření
plt.errorbar(N_kmity, Tk_hodnoty, yerr=Tk_chyby, fmt='o', color='#8b0000', 
             ecolor='black', elinewidth=2, capsize=6, capthick=2, 
             markersize=8, label='Změřené Tk s mezemi chyby')

# Přidání vizuálního "koridoru" chyby kolem nejpřesnějšího (posledního) měření
# Toto ukáže, k jaké hodnotě to konverguje
best_Tk = Tk_hodnoty[-1]
plt.axhline(y=best_Tk, color='#2b2b2b', linestyle='--', alpha=0.7, 
            label=f'Konvergující hodnota ({best_Tk:.4f} s)')

plt.fill_between(N_kmity, 
                 [best_Tk - Tk_chyby[-1]] * len(N_kmity), 
                 [best_Tk + Tk_chyby[-1]] * len(N_kmity), 
                 color='gray', alpha=0.2, label='Finální interval spolehlivosti')

# Formátování grafu
plt.title('Zpřesňování doby kyvu omezovací metodou (rotor elektromotoru)', fontsize=14, fontweight='bold')
plt.xlabel('Počet kmitů $N$ [-]', fontsize=12)
plt.ylabel('Doba jednoho kyvu $T_k$ [s]', fontsize=12)

# Osa X vypadá lépe s logaritmickým měřítkem (nebo specifickými ticky), 
# protože body 10, 20, 50, 100 jsou nerovnoměrně rozložené. Nastavíme pevné ticky:
plt.xticks(N_kmity)

plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='best')
plt.tight_layout()

# Zobrazení
plt.show()