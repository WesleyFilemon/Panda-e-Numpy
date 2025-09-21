# Atividade 8: Trabalhando com Datas
#Objetivo: Manipular dados temporais com Pandas.
# Dados de vendas diárias
#datas = pd.date_range('2024-01-01', periods=30, freq='D')
#vendas_diarias = np.random.randint(100, 500, 30)

import numpy as np
import pandas as pd
# TODO:
# 1. Criar DataFrame com datas como índice
# 2. Adicionar colunas: dia_semana, mes, trimestre
# 3. Filtrar apenas vendas de fins de semana
# 4. Calcular média de vendas por dia da semana
# 5. Encontrar a semana com maiores vendas
# 6. Criar coluna indicando se é 'weekday' ou 'weekend'

datas = pd.date_range('2024-01-01', periods=30, freq='D')
vendas_diarias = np.random.randint(100, 500, 30)


# Dados
datas = pd.date_range('2024-01-01', periods=30, freq='D')
vendas_diarias = np.random.randint(100, 500, 30)

# 1. Criar DataFrame com datas como índice
df_vendas = pd.DataFrame({'vendas': vendas_diarias}, index=datas)
print("DataFrame inicial:")
print(df_vendas.head())

# 2. Adicionar colunas: dia_semana, mes, trimestre
df_vendas['dia_semana'] = df_vendas.index.day_name(locale='pt_BR')  # nome do dia em português
df_vendas['mes'] = df_vendas.index.month
df_vendas['trimestre'] = df_vendas.index.quarter
print("\nDataFrame com colunas adicionais:")
print(df_vendas.head())

# 3. Filtrar apenas vendas de fins de semana (sábado e domingo)
fins_semana = df_vendas[df_vendas['dia_semana'].isin(['sábado', 'domingo'])]
print("\nVendas em fins de semana:")
print(fins_semana)

# 4. Calcular média de vendas por dia da semana
media_por_dia = df_vendas.groupby('dia_semana')['vendas'].mean()
print("\nMédia de vendas por dia da semana:")
print(media_por_dia)

# 5. Encontrar a semana com maiores vendas
df_vendas['semana'] = df_vendas.index.isocalendar().week
semana_mais_vendas = df_vendas.groupby('semana')['vendas'].sum().idxmax()
print(f"\nSemana com maiores vendas: {semana_mais_vendas}")

# 6. Criar coluna indicando se é 'weekday' ou 'weekend'
df_vendas['tipo_dia'] = np.where(df_vendas['dia_semana'].isin(['sábado', 'domingo']),
                                 'weekend', 'weekday')
print("\nDataFrame final com coluna weekday/weekend:")
print(df_vendas.head(10))