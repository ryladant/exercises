import matplotlib.pyplot as plt

# Dados para a reta (y = 2x + 1)
x = [0, 1, 2, 3, 4, 5]  # Valores de x
y = [2 * i + 1 for i in x]  # Valores de y calculados pela equação

# Criando o gráfico
plt.plot(x, y, label='y = 2x + 1', color='blue', linestyle='-', linewidth=2)

# Configurações do gráfico
plt.title("Gráfico de uma Reta (y = 2x + 1)")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Linha horizontal (eixo X)
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Linha vertical (eixo Y)
plt.grid(True, linestyle='--', alpha=0.5)  # Grade no gráfico
plt.legend()  # Legenda
plt.show()

