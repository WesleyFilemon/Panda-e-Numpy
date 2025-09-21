#Atividade 4: Criando DataFrames Básicos
#Objetivo: Criar e explorar estruturas de DataFrames.
# Dados de funcionários
#dados_funcionarios = {
#'nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
#'idade': [28, 35, 42, 29, 38],
#'salario': [3500, 4200, 5500, 3800, 4800],
#'departamento': ['TI', 'RH', 'TI', 'Marketing', 'TI']}

import numpy as np
import pandas as pd

# TODO:
# 1. Criar o DataFrame
# 2. Exibir informações básicas (shape, info, describe)
# 3. Mostrar apenas funcionários do departamento TI
# 4. Adicionar uma nova coluna 'bonus' (10% do salário)
# 5. Criar uma coluna 'categoria_idade': 'Jovem' (<30) ou 'Experiente' (>=30)
# 6. Remover a coluna 'departamento'

dados_funcionarios = {
'nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
'idade': [28, 35, 42, 29, 38],
'salario': [3500, 4200, 5500, 3800, 4800],
'departamento': ['TI', 'RH', 'TI', 'Marketing', 'TI']}

# 1. Criar o DataFrame
df = pd.DataFrame(dados_funcionarios)

# 2. Exibir informações básicas
print("Shape do DataFrame:", df.shape)
print("\nInformações do DataFrame:")
print(df.info())
print("\nEstatísticas descritivas:")
print(df.describe())

# 3. Mostrar apenas funcionários do departamento TI
funcionarios_ti = df[df['departamento'] == 'TI']
print("\nFuncionários do departamento TI:")
print(funcionarios_ti)

# 4. Adicionar uma nova coluna 'bonus' (10% do salário)
df['bonus'] = df['salario'] * 0.10
print("\nDataFrame com coluna 'bonus':")
print(df)

# 5. Criar uma coluna 'categoria_idade': 'Jovem' (<30) ou 'Experiente' (>=30)
df['categoria_idade'] = df['idade'].apply(lambda x: 'Jovem' if x < 30 else 'Experiente')
print("\nDataFrame com coluna 'categoria_idade':")
print(df)

# 6. Remover a coluna 'departamento'
df = df.drop('departamento', axis=1)
print("\nDataFrame após remover a coluna 'departamento':")
print(df)