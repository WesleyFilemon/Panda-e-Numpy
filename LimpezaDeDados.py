#Atividade 9: Limpeza de Dados
#Objetivo: Tratar valores ausentes e duplicados.
# DataFrame com dados "sujos"
#dados_sujos = pd.DataFrame({
#'nome': ['João', 'Maria', 'João', 'Pedro', None, 'Ana', 'Maria'],
#'idade': [25, None, 25, 30, 28, None, 35],
#'salario': [3000, 4000, 3000, None, 3500, 4500, 4000],
#'cidade': ['SP', 'RJ', 'SP', 'MG', 'SP', None, 'RJ']})

import numpy as np
import pandas as pd
# TODO:
# 1. Identificar linhas duplicadas
# 2. Remover duplicatas completas
# 3. Preencher idades ausentes com a média
# 4. Preencher salários ausentes com a mediana
# 5. Preencher cidades ausentes com 'Não informado'
# 6. Remover linhas onde nome é nulo

dados_sujos = pd.DataFrame({
'nome': ['João', 'Maria', 'João', 'Pedro', None, 'Ana', 'Maria'],
'idade': [25, None, 25, 30, 28, None, 35],
'salario': [3000, 4000, 3000, None, 3500, 4500, 4000],
'cidade': ['SP', 'RJ', 'SP', 'MG', 'SP', None, 'RJ']})

# 1. Identificar linhas duplicadas
duplicadas = dados_sujos[dados_sujos.duplicated()]
print("\nLinhas duplicadas:")
print(duplicadas)

# 2. Remover duplicatas completas
df_limpo = dados_sujos.drop_duplicates().copy()
print("\nDataFrame sem duplicatas:")
print(df_limpo)

# 3. Preencher idades ausentes com a média
media_idade = df_limpo['idade'].mean()
df_limpo['idade'] = df_limpo['idade'].fillna(media_idade)

# 4. Preencher salários ausentes com a mediana
mediana_salario = df_limpo['salario'].median()
df_limpo['salario'] = df_limpo['salario'].fillna(mediana_salario)

# 5. Preencher cidades ausentes com 'Não informado'
df_limpo['cidade'] = df_limpo['cidade'].fillna('Não informado')

# 6. Remover linhas onde nome é nulo
df_limpo = df_limpo.dropna(subset=['nome'])

print("\nDataFrame final limpo:")
print(df_limpo)