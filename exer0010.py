import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definindo os vértices do cubo
vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

# Definindo as arestas (conexões entre os vértices)
arestas = [
    [0, 1], [1, 2], [2, 3], [3, 0],  # face inferior
    [4, 5], [5, 6], [6, 7], [7, 4],  # face superior
    [0, 4], [1, 5], [2, 6], [3, 7]   # arestas verticais
]

# Criando a plotagem 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotando as arestas
for aresta in arestas:
    ax.plot([vertices[aresta[0]][0], vertices[aresta[1]][0]],
            [vertices[aresta[0]][1], vertices[aresta[1]][1]],
            [vertices[aresta[0]][2], vertices[aresta[1]][2]], 'b-')

# Definindo os limites dos eixos
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Exibindo o gráfico
plt.show()

