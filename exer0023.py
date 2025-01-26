import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# Gerar dados simulados para treinamento (y = 2x + 1)
X_train = np.array([1, 2, 3, 4, 5])  # Entradas (x)
y_train = 2 * X_train + 1  # Saídas (y) baseadas na função y = 2x + 1

# Construir o modelo da rede neural
model = models.Sequential([
    layers.Dense(1, input_dim=1, activation='linear')  # Uma camada densa, com 1 neurônio
])

# Compilar o modelo com um otimizador e uma função de perda (erro quadrático médio)
model.compile(optimizer='sgd', loss='mean_squared_error')

# Treinar o modelo
model.fit(X_train, y_train, epochs=500, verbose=0)

# Mostrar os pesos e vieses após o treinamento
weights, biases = model.layers[0].get_weights()
print(f"Pesos finais: {weights}")
print(f"Viés final: {biases}")

# Testar o modelo em novos dados
X_test = np.array([6, 7, 8])
y_pred = model.predict(X_test)
print(f"Previsões para novos dados: {y_pred}")

