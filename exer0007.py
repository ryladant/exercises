palavras = ["casa", "avião", "inteligência", "sol", "programação", "mar"]

palavras_acima_5_letras = [palavra for palavra in palavras if len(palavra) >= 5]

print(palavras_acima_5_letras)
