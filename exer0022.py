from gensim.models import Word2Vec

# Corpus de exemplo
sentences = [["eu", "gosto", "de", "programar"], ["programar", "é", "legal"], ["eu", "gosto", "de", "python"]]

# Treinando o modelo Word2Vec
model = Word2Vec(sentences, min_count=1)

# Pegando o embedding da palavra "programar"
embedding_programar = model.wv['programar']
print(embedding_programar)
