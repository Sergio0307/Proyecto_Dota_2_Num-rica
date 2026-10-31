"""
Implementa la interpolación de Lagrange para estimar el oro
en minutos no medidos, a partir de datos discretos.

Genera: figuras/interpolacion.pdf y figuras/interpolacion.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ---------- Función de Interpolación de Lagrange ----------
def lagrange(x_puntos, y_puntos, x):
    """Evalúa el polinomio de Lagrange en x."""
    total = 0.0
    n = len(x_puntos)
    for i in range(n):
        term = y_puntos[i]
        for j in range(n):
            if i != j:
                term *= (x - x_puntos[j]) / (x_puntos[i] - x_puntos[j])
        total += term
    return total

# ---------- Datos medidos (Ejemplo) ----------
# En la práctica, estos datos podrían venir de tu CSV
x_puntos = [5, 10, 15]
y_puntos = [1200, 2800, 4500]

# Queremos estimar el oro en el minuto 12
x_est = 12
y_est = lagrange(x_puntos, y_puntos, x_est)
print(f"Oro estimado en el minuto {x_est} usando interpolación: {y_est:.2f}")

# ---------- Gráfico ----------
# Creamos un rango de valores X para dibujar la curva continua
x_graf = np.linspace(4, 16, 100)
y_graf = [lagrange(x_puntos, y_puntos, x) for x in x_graf]

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_graf, y_graf, 'b-', label='Curva interpolada (Polinomio)')
ax.plot(x_puntos, y_puntos, 'ro', markersize=8, label='Datos medidos (5, 10, 15)')
ax.plot(x_est, y_est, 'g*', markersize=15, label=f'Estimación en minuto {x_est}')

# Detalles estéticos
ax.set_xlabel('Minuto de la partida')
ax.set_ylabel('Oro acumulado')
ax.set_title('Interpolación de Lagrange del oro acumulado')
ax.legend()
ax.grid(True, alpha=0.3)

# ---------- Guardar figura (CORREGIDO) ----------
# Usamos rutas absolutas para que no falle en Windows y guardamos ANTES de mostrar
ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_figuras = os.path.join(ruta_actual, '..', 'figuras')
os.makedirs(ruta_figuras, exist_ok=True)

plt.tight_layout()
# Guardamos primero el PNG y luego el PDF
plt.savefig(os.path.join(ruta_figuras, 'interpolacion.png'), dpi=150)
plt.savefig(os.path.join(ruta_figuras, 'interpolacion.pdf'))

# Cerramos el gráfico en memoria
plt.close()

print("¡Gráficos de interpolación guardados con éxito!")