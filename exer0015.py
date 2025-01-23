# 1. Importando bibliotecas
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 2. Carregando o dataset Iris
iris = load_iris()
X = iris.data  # Características (features)
y = iris.target  # Classes (labels)

# 3. Dividindo em treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Criando e treinando o modelo (K-Nearest Neighbors)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# 5. Fazendo previsões
y_pred = model.predict(X_test)

# 6. Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {accuracy:.2f}")

# Extra: Teste o modelo com novos dados
new_data = [[5.1, 3.5, 1.4, 0.2]]  # Um exemplo de medidas
prediction = model.predict(new_data)
print(f"Previsão para o novo dado: {iris.target_names[prediction][0]}")

