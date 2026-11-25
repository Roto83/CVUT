Abychom vypočítali odchylku, odečteme hodnoty, které jsme vypočítali z kroků ADC (v jednotkách Volt), od tvých vstupních napjatí (která jsou v tomto případě uvedena v mV).

Pro přehlednosti přepočítám výpočty z předchozího kroku na **mV** a porovnám je přímo s tvými daty:

| Vstupní napětí [mV] | Výpočet ADC [mV] | Odchylka [mV] |
| :------------------ | :--------------- | :------------ |
| **6**               | 0,00             | **6,00**      |
| **61**              | 39,06            | **21,94**     |
| **1003**            | 976,56           | **26,44**     |
| **2503**            | 2500,00          | **3,00**      |
| **5008**            | 5000,00          | **8,00**      |
| **7507**            | 7500,00          | **7,00**      |
| **9006**            | 8984,38          | **21,62**     |
| **9904**            | 9885,94          | **18,06**     |

### Jak jsem to počítal:
1.  **Výpočet ADC [mV]:** Vzala jsem hodnoty z předchozí tabulky (např. $2,5\text{ V}$) a převedla je na milivolty ($2,5 \times 1000 = 2500$).
2.  **Odchylka:** Vypočítána jako absolutní rozdíl $|V_{vstup} - V_{výpočet}|$.

*Poznámka: Zaokrouhleno na dvě desetinná místa.*