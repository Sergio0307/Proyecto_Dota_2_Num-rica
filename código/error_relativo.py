"""
Calcula el error relativo E_r(T) para los tres héroes
y genera la gráfica de evolución temporal.

Genera: figuras/error_relativo.pdf y datos/error_relativo_calculado.csv
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------- Funciones del modelo (iguales a fopt.py) ----------
def c_melee(t): return 3 + (t >= 15) + (t >= 30) + (t >= 45)
def c_ranged(t): return 1 + (t >= 40)
def g_oleada(t): return 36 * c_melee(t) + 48 * c_ranged(t)
def f_opt(T, r=0.5, g_camp=78):
    return sum(g_oleada(k / 2) for k in range(2 * T)) + r * g_camp * T

# ---------- Cargar datos reales ----------
# Asegúrate de ejecutar este script desde la carpeta 'codigo'
try:
    df_real = pd.read_csv('../datos/farmeo_real.csv')
except FileNotFoundError:
    print("Error: No se encontró el archivo '../datos/farmeo_real.csv'.")
    print("Asegúrate de estar en la carpeta 'codigo' al ejecutar el script.")
    exit()

# ---------- Calcular error por héroe y minuto ----------
resultados = []
for heroe in df_real['heroe'].unique():
    sub = df_real[df_real['heroe'] == heroe].sort_values('minuto')
    for _, row in sub.iterrows():
        T = int(row['minuto'])
        Fo = f_opt(T)
        Fr = row['oro_real']
        # Fórmula del error relativo
        Er = abs(Fo - Fr) / Fo * 100 
        resultados.append({'heroe': heroe, 'minuto': T,
                           'F_opt': round(Fo), 'F_real': Fr, 'E_r': round(Er, 2)})

df_err = pd.DataFrame(resultados)
df_err.to_csv('../datos/error_relativo_calculado.csv', index=False)

# ---------- Gráfico ----------
fig, ax = plt.subplots(figsize=(10, 6))
colores = {'Sven': 'blue', 'Luna': 'green', 'Templar': 'purple'}

for heroe in df_err['heroe'].unique():
    sub = df_err[df_err['heroe'] == heroe]
    ax.plot(sub['minuto'], sub['E_r'], marker='o', label=heroe, 
            color=colores.get(heroe, 'black'))

# Línea de umbral crítico (ej. 30% de error)
ax.axhline(y=30, color='gray', linestyle='--', label='Umbral crítico 30%')

ax.set_xlabel('Minuto de la partida')
ax.set_ylabel('Error relativo \(E_r\) (%)')
ax.set_title('Evolución del error relativo por héroe')
ax.legend()
ax.grid(True, alpha=0.3)

# Guardar figura
os.makedirs('../figuras', exist_ok=True)
plt.tight_layout()
plt.savefig('../figuras/error_relativo.pdf')
plt.savefig('../figuras/error_relativo.png', dpi=150)
plt.show()

# ---------- Imprimir tabla en consola ----------
print("\n--- Tabla de Error Relativo Calculado ---")
print(df_err.to_string(index=False))