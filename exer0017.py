#Desenhe o grafico da função y = 5x + 7

import matplotlib.pyplot as plt
import numpy as np

# Gerando valores de x
x = np.linspace(-10, 10, 100)  # Valores de x no intervalo [-10, 10], com 100 pontos

# Calculando y = 5x + 7
y = 5 * x + 7

# Criando o gráfico
plt.plot(x, y, label="y = 5x + 7", color="blue", linestyle="-")

# Adicionando rótulos e título
plt.title("Gráfico da Função y = 5x + 7")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Linha do eixo x
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")  # Linha do eixo y
plt.grid(True, linestyle="--", alpha=0.6)  # Adiciona grade
plt.legend()  # Mostra a legenda
plt.show()  # Exibe o gráfico
