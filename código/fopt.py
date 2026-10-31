"""
Genera una gráfica comparativa del farmeo óptimo (Inmortal)
vs el farmeo real (Promedio) para Sven, Luna y Templar Assassin.

Genera: figuras/fopt_vs_freal.pdf y figuras/fopt_vs_freal.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ---------- Datos (Extraídos de benchmarks reales) ----------
T_vals = np.array([10, 15, 20])

# Óptimo (Inmortal)
Luna_Opt = np.array([5600, 9800, 15000])
Templar_Opt = np.array([5400, 9200, 13500])
Sven_Opt = np.array([5000, 8500, 14000])

# Promedio (Medallas bajas)
Luna_Prom = np.array([3700, 7300, 9300])
Templar_Prom = np.array([3800, 8200, 9400])
Sven_Prom = np.array([3500, 6500, 8900])

# Last Hits (usaremos los del jugador promedio para las marcas)
LH_Sven_Prom = np.array([65, 130, 190])
LH_Luna_Prom = np.array([70, 152, 200])
LH_Templar_Prom = np.array([75, 150, 194])

# ---------- Gráfico Comparativo ----------
fig, ax = plt.subplots(figsize=(10, 6))

# Líneas de Óptimo (Inmortales) - Sólidas
ax.plot(T_vals, Luna_Opt, 'g-', linewidth=3, marker='o', label='Luna (Óptimo)')
ax.plot(T_vals, Templar_Opt, 'm-', linewidth=3, marker='o', label='Templar (Óptimo)')
ax.plot(T_vals, Sven_Opt, 'c-', linewidth=3, marker='o', label='Sven (Óptimo)')

# Líneas Promedio - Punteadas
ax.plot(T_vals, Luna_Prom, 'g--', linewidth=2, marker='x', label='Luna (Promedio)')
ax.plot(T_vals, Templar_Prom, 'm--', linewidth=2, marker='x', label='Templar (Promedio)')
ax.plot(T_vals, Sven_Prom, 'c--', linewidth=2, marker='x', label='Sven (Promedio)')

# Relleno entre Óptimo y Promedio (El "Error" o brecha de farmeo)
ax.fill_between(T_vals, Luna_Prom, Luna_Opt, color='green', alpha=0.1)
ax.fill_between(T_vals, Templar_Prom, Templar_Opt, color='magenta', alpha=0.1)
ax.fill_between(T_vals, Sven_Prom, Sven_Opt, color='cyan', alpha=0.1)

ax.set_xlabel('Tiempo T (minutos)')
ax.set_ylabel('Oro acumulado')
ax.set_title('Farmeo Óptimo (Inmortal) vs Promedio (Medalla baja)')
ax.legend(loc='upper left', ncol=2)
ax.grid(True, alpha=0.3)

# Añadir un eje secundario para los Last Hits del jugador promedio
ax2 = ax.twinx()
ax2.plot(T_vals, LH_Luna_Prom, 'g^', alpha=0.5, linestyle='None', markersize=8)
ax2.plot(T_vals, LH_Templar_Prom, 'm^', alpha=0.5, linestyle='None', markersize=8)
ax2.plot(T_vals, LH_Sven_Prom, 'c^', alpha=0.5, linestyle='None', markersize=8)
ax2.set_ylabel('Last Hits del Promedio (Triángulos)')
ax2.set_ylim(0, 350) # Ajuste de escala

# ---------- Guardar figura ----------
ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_figuras = os.path.join(ruta_actual, '..', 'figuras')
os.makedirs(ruta_figuras, exist_ok=True)

plt.tight_layout()
plt.savefig(os.path.join(ruta_figuras, 'fopt_vs_freal.png'), dpi=150)
plt.savefig(os.path.join(ruta_figuras, 'fopt_vs_freal.pdf'))
plt.close()

print("¡Gráfico comparativo (Inmortal vs Promedio) generado con éxito!")