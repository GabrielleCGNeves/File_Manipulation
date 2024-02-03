import pandas as pd

#Declaração da variável dara
data = {'Nome': ['Matheus', 'Rafael', 'Lucas'],
        'Recorde': [98, 100, 70],
        'Pontos': [218, 245, 160]}

print(data)

#Criando o dataframe a partir dos dados da variável data
df = pd.DataFrame(data)
print(df)

#Mostra o índice da linha
print(df.loc[0])

#Mostrar o índice de mais uma linha
print(df.loc[[0,1]])

#Criando indice personalizado
df = pd.DataFrame(data, index=['Rank1', 'Rank2', 'Rank3'])

#Mostra o conteúdo do índice
print(df.loc["Rank3"])

#Imprime informações do dataframe
print(df.info())

#Imprime o dataframe
print(df)

#Imprime a descrição do dataframe
df.describe()