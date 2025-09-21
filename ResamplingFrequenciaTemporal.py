#Atividade 17: Resampling e Frequência Temporal
#Objetivo: Trabalhar com agregações temporais.
# Dados de vendas horárias
#datas_horarias = pd.date_range('2024-01-01 00:00:00',
#periods=168, freq='H') # 1 semana
#vendas_horarias = pd.DataFrame({
#'timestamp': datas_horarias,
#'vendas': np.random.poisson(10, 168) + np.random.randint(0, 5, 168)})
#vendas_horarias.set_index('timestamp', inplace=True)

# TODO:
# 1. Agrupar vendas por dia (soma diária)
# 2. Calcular média de vendas por hora do dia
# 3. Encontrar o dia da semana com maiores vendas
# 4. Calcular vendas por período: manhã (6-12h), tarde (12-18h), noite (18-24h)
# 5. Identificar padrões de sazonalidade
# 6. Calcular média móvel de 24 horas

import pandas as pd
import numpy as np

# Dados
datas_horarias = pd.date_range('2024-01-01 00:00:00', periods=168, freq='H')  # 1 semana
vendas_horarias = pd.DataFrame({
    'timestamp': datas_horarias,
    'vendas': np.random.poisson(10, 168) + np.random.randint(0, 5, 168)
})
vendas_horarias.set_index('timestamp', inplace=True)

# 1. Agrupar vendas por dia (soma diária)
vendas_diarias = vendas_horarias.resample('D').sum()
print("\n1. Vendas diárias:")
print(vendas_diarias)

# 2. Média de vendas por hora do dia
vendas_horarias['hora'] = vendas_horarias.index.hour
media_por_hora = vendas_horarias.groupby('hora')['vendas'].mean()
print("\n2. Média de vendas por hora do dia:")
print(media_por_hora)

# 3. Dia da semana com maiores vendas
vendas_horarias['dia_semana'] = vendas_horarias.index.day_name()
total_por_dia = vendas_horarias.groupby('dia_semana')['vendas'].sum()
dia_maior_venda = total_por_dia.idxmax()
print("\n3. Dia da semana com maiores vendas:", dia_maior_venda)

# 4. Vendas por período do dia
def periodo_horario(h):
    if 6 <= h < 12:
        return 'Manhã'
    elif 12 <= h < 18:
        return 'Tarde'
    elif 18 <= h < 24:
        return 'Noite'
    else:
        return 'Madrugada'

vendas_horarias['periodo'] = vendas_horarias['hora'].apply(periodo_horario)
vendas_periodo = vendas_horarias.groupby('periodo')['vendas'].sum()
print("\n4. Vendas por período do dia:")
print(vendas_periodo)

# 5. Identificar padrões de sazonalidade
# Média por hora do dia por dia da semana
padrão_sazonal = vendas_horarias.pivot_table(index='hora', columns='dia_semana', values='vendas', aggfunc='mean')
print("\n5. Padrão de sazonalidade (média por hora x dia da semana):")
print(padrão_sazonal)

# 6. Média móvel de 24 horas
vendas_horarias['media_movel_24h'] = vendas_horarias['vendas'].rolling(window=24).mean()
print("\n6. Média móvel de 24 horas (últimas 10 linhas):")
print(vendas_horarias.tail(10))
