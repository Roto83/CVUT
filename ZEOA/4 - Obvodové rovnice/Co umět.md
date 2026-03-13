Metoda smyčkových proudů
Metoda uzlových napětí

## Zopakovat
Proudový a napěťový dělič, osvojit vzorce atd.


```tikz
\usepackage[european, straightvoltages]{circuitikz}
\begin{document}
\begin{circuitikz}
    % Stejnosměrný zdroj a první rezistor
    \draw (0,0) to[V, v=$U_s=60\,\mathrm{V}$] (0,4)
          to[R, l=$R_1=10\,\Omega$, i=$I_{celk}$] (3,4) coordinate (A) node[circ]{} node[above]{A};

    % Levá paralelní větev (R2)
    \draw (A) to[short] (3,3)
          to[R, l=$R_2=20\,\Omega$, i=$I_2$] (3,1)
          to[short] (3,0) coordinate (B) node[circ]{} node[below]{B};

    % Pravá paralelní větev (R3 a R4 v sérii)
    \draw (A) to[short] (6,4)
          to[R, l=$R_3=5\,\Omega$] (6,2)
          to[R, l=$R_4=15\,\Omega$, v=$U_4$] (6,0)
          to[short] (B);

    % Uzavření obvodu zpět ke zdroji
    \draw (B) to[short] (0,0);
\end{circuitikz}
\end{document}
```
```tikz
\usepackage{circuitikz}
\begin{document}

\begin{circuitikz}[american, voltage shift=0.5]
\draw (0,0)
to[isource, l=$I_0$, v=$V_0$] (0,3)
to[short, -*, i=$I_0$] (2,3)
to[R=$R_1$, i>_=$i_1$] (2,0) -- (0,0);
\draw (2,3) -- (4,3)
to[R=$R_2$, i>_=$i_2$]
(4,0) to[short, -*] (2,0);
\end{circuitikz}

\end{document}
```
