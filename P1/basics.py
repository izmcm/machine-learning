from dados import acessos
from sklearn.naive_bayes import MultinomialNB

X, Y = acessos()

modelo = MultinomialNB() # criando modelo
modelo.fit(X, Y)

pessoa = [[1, 0, 1]]
print(modelo.predict(pessoa))