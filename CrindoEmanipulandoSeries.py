# Atividade 1: Criando e Manipulando Series
#Objetivo: Criar uma Series com dados de vendas e praticar operações básicas.
# Crie uma Series com vendas diárias de uma loja (7 dias)
#vendas = [1200, 1500, 800, 2000, 1800, 2200, 1600]
#dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

# TODO:
# 1. Criar a Series com índices personalizados (dias da semana)
# 2. Exibir apenas as vendas de terça e sexta
# 3. Adicionar um novo dia (Feriado) com valor 500
# 4. Alterar o valor de 'Quarta' para 900
# 5. Remover o domingo da Series
# 6. Calcular a média de vendas da semana

import numpy as np
import pandas as pd


# 1. Criar a Series com índices personalizados (dias da semana)
dias_semana = np.array(['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom'])
vendas = np.array([1200, 1500, 800, 2000, 1800, 2200, 1600])
serie_vendas = pd.Series(vendas, index=dias_semana)

print("Vendas da semana:")
print(serie_vendas)

# 2. Exibir apenas as vendas de terça e sexta
vendas_ter_sex = serie_vendas[['Ter', 'Sex']]
print("\nVendas de Terça e Sexta:")
print(vendas_ter_sex)

# 3. Adicionar um novo dia (Feriado) com valor 500
serie_vendas["Feriado"] = 500

print("\nFeriado adicionado:")
print(serie_vendas)

# 4. Alterar o valor de 'Quarta' para 900
serie_vendas['Qua'] = 900

print("\nValor da Quarta alterado:")
print(serie_vendas)

# 5. Remover o domingo da Series
serie_vendas = serie_vendas.drop("Dom")

print("\nDomingo removido:")
print(serie_vendas)

# 6. Calcular a média de vendas da semana
media_diaria = np.mean(vendas)

print("\nMedia da semana:")
print(round(media_diaria, 2))