import pandas as pd
# from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier

dados = pd.read_csv("busca.csv")

Y_df = dados['comprou']
X_df = dados[['home', 'busca', 'logado']]

Xdummies_df = pd.get_dummies(X_df)

X_arr = Xdummies_df.values
Y_arr = Y_df.values

# treinando com 90% dos dados
treinoX = X_arr[:900]
treinoY = Y_arr[:900]

# testando com 10% dos dados
testeX = X_arr[-100:]
testeY = Y_arr[-100:]

modelo = AdaBoostClassifier()
modelo.fit(treinoX, treinoY) # treinando

ans = modelo.predict(testeX)

diff = ans - testeY

tot_acertos = 0
for i in diff:
    if i == 0:
        tot_acertos += 1

tot_elem = len(testeX)

taxa_acerto = 100.0*(tot_acertos/tot_elem)

print(taxa_acerto)
print(tot_elem)
