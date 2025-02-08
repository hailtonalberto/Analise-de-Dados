#importar a base de dados
# vizualizar a base de dados
    #entender oque tem nas base de dados
    #encontrar as cagadas na base de dados
# corrigir as cagadas da base de dados
#anlise inicial e cancelamento da dados não util
#tirar a coluna de customerID
#analise causas porque o cancelamento dos clientes
#clonunas inuteis
#informações no formato errado
#valores vazio
import pandas
from PIL._imaging import display

tabela = pandas.read_csv("cancelamentos.csv")
#eliminar colunas customer
tabela = tabela.drop(columns="CustomerID")

print(tabela)

#informações de casas decimais e colunas de textos
tabela.info()

#elimina as linhas vazias das colunas
tabela = tabela.dropna()

# esse codigo é para ver quem cancelou e quem não cancelou
print(tabela["cancelou"].value_counts())

#esse codigo le em porcentagem
print(tabela["cancelou"].value_counts(normalize=True))

import plotly.express as px

coluna = tabela.columns
for coluna in tabela.columns:

    #criar grafico
    grafico = px.histogram(tabela,x=coluna,color="cancelou")

    #exibir grafico
    grafico.show()