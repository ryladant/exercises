#Crie uma lista contendo o quadrado de todos os números pares de 1 a 20

numeros = [x**2 for x in range(1,21) if x%2==0]

print(numeros)
