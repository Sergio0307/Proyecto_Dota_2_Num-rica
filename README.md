# Optimización del farmeo en Dota 2 mediante Matemática Numérica

Proyecto académico que modela la obtención de oro en Dota 2 (oleadas de línea
y campamentos neutrales) y calcula la ruta de farmeo óptima para tres héroes:
**Sven**, **Luna** y **Templar Assassin**.

El objetivo es medir, con herramientas de Matemática Numérica (interpolación,
error relativo, optimización sobre grafos), qué tan lejos está el farmeo real
de un jugador del farmeo teórico óptimo, y diseñar un croquis de ruta que
reduzca esa diferencia.

---

## Estructura del proyecto
proyecto_dota_numerico/
├── README.md
├── datos/
├── codigo/
├── figuras/
├── documento/
└── presentacion/

text

---

## Datos base utilizados

| Elemento | Valor | Fuente |
|---|---|---|
| Spawn de oleadas de línea | cada 30 s | Dota 2 Wiki |
| Composición inicial | 3 melee + 1 ranged | Dota 2 Wiki |
| +1 melee | minutos 15, 30, 45 | Dota 2 Wiki |
| +1 ranged | minuto 40 | Dota 2 Wiki |
| Oro por melee | ~36 | Dota 2 Wiki |
| Oro por ranged | ~48 | Dota 2 Wiki |
| Spawn de campamentos neutrales | cada 60 s | Dota 2 Wiki |
| Ventana de stacking | :53 – :55 | Dota 2 Wiki |
| Oro campamento Small | ~55 | Dota 2 Wiki |
| Oro campamento Medium | ~78 | Dota 2 Wiki |
| Oro campamento Large | ~100 | Dota 2 Wiki |

---

## Función principal del modelo

F_opt(T) = suma de oleadas en T minutos + r * 78 * T

E_r(T) = |F_opt(T) - F_real(T)| / F_opt(T) * 100%

---

## Héroes de estudio

| Héroe | Estilo de farmeo | Habilidad clave |
|---|---|---|
| Sven | Cuerpo a cuerpo, daño en área | Great Cleave |
| Luna | A distancia, ataques con rebote | Moon Glaive |
| Templar Assassin | A distancia, daño en línea recta | Psi Blades / Refraction |

---

## Herramientas utilizadas

- **Python** (numpy, matplotlib, pandas, networkx)
- **LaTeX** (Beamer) para informe y diapositivas
- **Visual Studio Code** como entorno

---

## Cómo compilar

### Python
cd codigo
pip install -r requirements.txt
python fopt.py

### Informe
cd documento
pdflatex informe.tex
bibtex informe
pdflatex informe.tex
pdflatex informe.tex


### Presentación
cd presentacion
pdflatex slides.tex

