#Atividade 7: Operações com NumPy Arrays
#Objetivo: Integrar NumPy com operações em DataFrames.
# Dados de temperaturas
#temperaturas = np.array([
#[22, 25, 28, 30, 27], # Semana 1
#[20, 23, 26, 29, 25], # Semana 2
#[24, 27, 30, 32, 28], # Semana 3
#[21, 24, 27, 31, 26] # Semana 4])

import numpy as np
import pandas as pd

# TODO:
# 1. Converter para DataFrame com colunas ['Seg', 'Ter', 'Qua', 'Qui', 'Sex']
# 2. Calcular temperatura média por dia da semana
# 3. Encontrar o dia mais quente de cada semana
# 4. Criar uma coluna com a amplitude térmica de cada semana
# 5. Converter todas as temperaturas para Fahrenheit (F = C * 9/5 + 32)
# 6. Identificar dias com temperatura acima da média geral

temperaturas = np.array([
[22, 25, 28, 30, 27], # Semana 1
[20, 23, 26, 29, 25], # Semana 2
[24, 27, 30, 32, 28], # Semana 3
[21, 24, 27, 31, 26] # Semana 4])
])

# 1. Converter para DataFrame com colunas ['Seg', 'Ter', 'Qua', 'Qui', 'Sex']
df_temp = pd.DataFrame(temperaturas, columns=['Seg', 'Ter', 'Qua', 'Qui', 'Sex'])
print("DataFrame de temperaturas:")
print(df_temp)

# 2. Calcular temperatura média por dia da semana
media_dia = df_temp.mean()
print("\nTemperatura média por dia da semana:")
print(media_dia)

# 3. Encontrar o dia mais quente de cada semana
dia_mais_quente_semana = df_temp.idxmax(axis=1)
print("\nDia mais quente de cada semana:")
print(dia_mais_quente_semana)

# 4. Criar uma coluna com a amplitude térmica de cada semana (max - min)
df_temp['Amplitude'] = df_temp.max(axis=1) - df_temp.min(axis=1)
print("\nDataFrame com amplitude térmica de cada semana:")
print(df_temp)

# 5. Converter todas as temperaturas para Fahrenheit (F = C * 9/5 + 32)
df_temp_F = df_temp[['Seg','Ter','Qua','Qui','Sex']] * 9/5 + 32
df_temp_F['Amplitude'] = df_temp['Amplitude'] * 9/5  # amplitude também em F
print("\nTemperaturas em Fahrenheit:")
print(df_temp_F)

# 6. Identificar dias com temperatura acima da média geral
media_geral = df_temp[['Seg','Ter','Qua','Qui','Sex']].values.mean()
dias_acima_media = df_temp[['Seg','Ter','Qua','Qui','Sex']] > media_geral
print("\nDias com temperatura acima da média geral (True = acima):")
print(dias_acima_media)