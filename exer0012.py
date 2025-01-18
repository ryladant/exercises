#rotacionando um vetor (x, y) em theta graus.

import numpy as np
import matplotlib.pyplot as plt

vetor = np.array([2, 2])
theta = np.pi/4

matrix_rot = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

vetor_rot = np.dot(matrix_rot, vetor)

print(f"Vetor original: {vetor}")
print(f"Vetor Rotacionado: {vetor_rot}")

plt.figure()

#vetor original
plt.quiver(0, 0, vetor[0], vetor[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original')

#vetor rotacionado
plt.quiver(0,0,vetor_rot[0], vetor_rot[1], angles='xy', scale_units='xy', scale=1, color='green', label='rotacionado')

# Configurações do gráfico
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.grid()
plt.legend()
plt.title('Vetor Original e Rotacionado')
plt.xlabel('X')
plt.ylabel('Y')

# Exibe o gráfico
plt.show()
