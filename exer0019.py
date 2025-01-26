import numpy as np
import matplotlib.pyplot as plt

# Dados de entrada (tamanho e preço)
x = np.array([50, 60, 70, 80, 90])  # tamanho da casa
y = np.array([150, 180, 210, 240, 270])  # preço da casa

# Parâmetros iniciais
m = 0  # coeficiente angular inicial
b = 0  # coeficiente linear inicial
alpha = 0.0001  # taxa de aprendizado
iterations = 1000  # número de iterações

# Função de erro (MSE)
def compute_cost(x, y, m, b):
    n = len(x)
    cost = (1 / (2 * n)) * np.sum((m * x + b - y) ** 2)
    return cost

# Gradiente Descendente
def gradient_descent(x, y, m, b, alpha, iterations):
    n = len(x)
    cost_history = []

    for i in range(iterations):
        # Cálculo do gradiente
        m_grad = -(1 / n) * np.sum(x * (y - (m * x + b)))
        b_grad = -(1 / n) * np.sum(y - (m * x + b))
        
        # Atualização dos parâmetros
        m = m - alpha * m_grad
        b = b - alpha * b_grad
        
        # Armazenar o valor da função de custo para visualização
        cost_history.append(compute_cost(x, y, m, b))

    return m, b, cost_history

# Treinamento do modelo
m_final, b_final, cost_history = gradient_descent(x, y, m, b, alpha, iterations)

# Exibindo os resultados
print(f"Coeficiente angular (m): {m_final}")
print(f"Coeficiente linear (b): {b_final}")

# Plotando o custo ao longo das iterações
plt.plot(range(iterations), cost_history)
plt.xlabel("Iterações")
plt.ylabel("Custo")
plt.title("Descida do Gradiente: Função de Custo")
plt.show()

# Plotando a linha de regressão
plt.scatter(x, y, color="blue", label="Dados reais")
plt.plot(x, m_final * x + b_final, color="red", label="Linha de regressão")
plt.xlabel("Tamanho (m²)")
plt.ylabel("Preço")
plt.title("Regressão Linear - Gradiente Descendente")
plt.legend()
plt.show()
