from deepface import DeepFace

# Verificar se dois rostos são da mesma pessoa
resultado = DeepFace.verify("foto1.jpg", "foto2.jpg")

# Exibir o resultado
print("É a mesma pessoa?" , resultado["verified"])
