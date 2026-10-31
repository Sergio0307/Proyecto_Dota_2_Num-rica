"""
Construye un grafo simplificado de rutas de farmeo y lo dibuja.

Genera: figuras/grafo_rutas.pdf y figuras/grafo_rutas.png
"""

import networkx as nx
import matplotlib.pyplot as plt
import os

# ---------- Construcción del grafo ----------
G = nx.DiGraph()

G.add_edge('linea', 'campA', tiempo=14, oro=78)
G.add_edge('campA', 'linea', tiempo=14, oro=0)
G.add_edge('linea', 'campB', tiempo=20, oro=78)
G.add_edge('campB', 'linea', tiempo=20, oro=0)
G.add_edge('campA', 'campB', tiempo=10, oro=78)
G.add_edge('campB', 'campC', tiempo=12, oro=78)

# ---------- Posiciones para el dibujo ----------
pos = {
    'linea': (0, 0),
    'campA': (1, 1),
    'campB': (2, 0.5),
    'campC': (3, 1),
}

# ---------- Dibujo del grafo ----------
fig, ax = plt.subplots(figsize=(8, 5))

nx.draw_networkx_nodes(G, pos, node_size=1500, node_color='lightblue', ax=ax)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', ax=ax)
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, 
                       edge_color='gray', width=2, ax=ax)

edge_labels = {(u, v): f"{d['tiempo']}s" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, 
                             font_size=9, label_pos=0.5, ax=ax)

ax.set_title('Grafo de rutas de farmeo (pesos = tiempo en segundos)')
ax.axis('off')

# ---------- Guardar figura (CORREGIDO) ----------
ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_figuras = os.path.join(ruta_actual, '..', 'figuras')
os.makedirs(ruta_figuras, exist_ok=True)

plt.tight_layout()
plt.savefig(os.path.join(ruta_figuras, 'grafo_rutas.png'), dpi=150)
plt.savefig(os.path.join(ruta_figuras, 'grafo_rutas.pdf'))
plt.close()

print("¡Gráfico del grafo de rutas guardado con éxito!")