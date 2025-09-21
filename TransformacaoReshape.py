#Atividade 11: Transformação e Reshape
#Objetivo: Remodelar dados com pivot, melt e transpose.
# Dados de vendas mensais por região
#vendas_regiao = pd.DataFrame({
#'regiao': ['Norte', 'Sul', 'Leste', 'Oeste'] * 3,
#'mes': ['Jan', 'Jan', 'Jan', 'Jan', 'Fev', 'Fev', 'Fev', 'Fev', 'Mar', 'Mar', 'Mar', 'Mar'],
#'vendas': [100, 150, 120, 130, 110, 160, 140, 135, 105, 155, 125, 140]})

import numpy as np
import pandas as pd
# TODO:
# 1. Criar tabela pivot com meses como colunas e regiões como linhas
# 2. Calcular total de vendas por região
# 3. Encontrar o mês com maiores vendas
# 4. Converter a tabela pivot de volta para formato longo (melt)
# 5. Criar uma nova coluna com crescimento mês a mês por região
# 6. Transpor a tabela pivot

vendas_regiao = pd.DataFrame({
    'regiao': ['Norte', 'Sul', 'Leste', 'Oeste'] * 3,
    'mes': ['Jan', 'Jan', 'Jan', 'Jan', 'Fev', 'Fev', 'Fev', 'Fev', 'Mar', 'Mar', 'Mar', 'Mar'],
    'vendas': [100, 150, 120, 130, 110, 160, 140, 135, 105, 155, 125, 140]
})

# 1. Criar tabela pivot
pivot = vendas_regiao.pivot_table(index='regiao', columns='mes', values='vendas')
print("\n1. Pivot Table (região x mês):")
print(pivot)

# 2. Calcular total de vendas por região
total_regiao = vendas_regiao.groupby('regiao')['vendas'].sum().reset_index()
print("\n2. Total de vendas por região:")
print(total_regiao)

# 3. Encontrar o mês com maiores vendas
total_mes = vendas_regiao.groupby('mes')['vendas'].sum()
mes_maior_venda = total_mes.idxmax()
print("\n3. Mês com maiores vendas:", mes_maior_venda)

# 4. Converter a tabela pivot para formato longo
melted = pivot.reset_index().melt(id_vars='regiao', var_name='mes', value_name='vendas')
print("\n4. Tabela no formato longo (melt):")
print(melted)

# 5. Criar coluna de crescimento mês a mês por região
pivot_sorted = pivot[['Jan','Fev','Mar']]  # garantir ordem dos meses
crescimento = pivot_sorted.pct_change(axis=1) * 100
print("\n5. Crescimento mês a mês (%):")
print(crescimento)

# 6. Transpor a tabela pivot
transposta = pivot.T
print("\n6. Tabela transposta:")
print(transposta)