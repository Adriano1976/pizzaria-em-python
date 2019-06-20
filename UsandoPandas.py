import pandas as pd
#O Pandas permite criar dataframe, que é uma forma de tabela, como pode ser visto a seguir
df =pd.read_csv('arquivo.csv', sep=';') #Importa o arquivo.csv usando o separador ; como divisor de colunas
print(df) #Exibe o dataframe
print(type(df)) #mostra o tipo de dado
print(df.head()) #mostra as primeiras linhas do dataframe
print(df.shape) #Mostra quantas linhas e colunas possui o dataframe
print(df.tail()) #Mostra as ultimas linhas de um dataframe
print(df.describe())
print(df.dtypes)
print(df['Journal Impact Factor'])
print(df[3:10])
print(df.sample(5))