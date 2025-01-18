#rotacionando um vetor (x, y) em theta graus.

import numpy as np

vetor = np.array([2, 2])
theta = np.pi / 2

matrix_rot = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

vetor_rot = np.dot(matrix_rot, vetor)

print(f"Vetor original: {vetor}")
print(f"Vetor Rotacionado: {vetor_rot}")
