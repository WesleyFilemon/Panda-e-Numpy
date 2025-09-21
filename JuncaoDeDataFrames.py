#Atividade 10: Junção de DataFrames
#Objetivo: Praticar merge, join e concatenação.
# DataFrames relacionados
#clientes = pd.DataFrame({
#'id_cliente': [1, 2, 3, 4, 5],
#'nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
#'cidade': ['SP', 'RJ', 'MG', 'SP', 'RJ']})

#pedidos = pd.DataFrame({
#'id_pedido': [101, 102, 103, 104, 105, 106],
#'id_cliente': [1, 2, 1, 3, 2, 4],
#'valor': [150, 200, 300, 100, 250, 180]})

import numpy as np
import pandas as pd
# TODO:
# 1. Fazer inner join entre clientes e pedidos
# 2. Fazer left join para mostrar todos os clientes
# 3. Calcular total de pedidos por cliente
# 4. Calcular valor médio de pedido por cidade
# 5. Identificar clientes sem pedidos
# 6. Criar ranking de clientes por valor total

clientes = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4, 5],
    'nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'cidade': ['SP', 'RJ', 'MG', 'SP', 'RJ']
})

pedidos = pd.DataFrame({
    'id_pedido': [101, 102, 103, 104, 105, 106],
    'id_cliente': [1, 2, 1, 3, 2, 4],
    'valor': [150, 200, 300, 100, 250, 180]
})

# 1. Inner join entre clientes e pedidos
inner_join = pd.merge(clientes, pedidos, on='id_cliente', how='inner')
print("\n1. Inner join (clientes com pedidos):")
print(inner_join)

# 2. Left join (todos os clientes, mesmo sem pedidos)
left_join = pd.merge(clientes, pedidos, on='id_cliente', how='left')
print("\n2. Left join (todos os clientes):")
print(left_join)

# 3. Total de pedidos por cliente
total_pedidos = pedidos.groupby('id_cliente')['valor'].sum().reset_index()
total_pedidos = total_pedidos.merge(clientes[['id_cliente', 'nome']], on='id_cliente')
print("\n3. Total de pedidos por cliente:")
print(total_pedidos)

# 4. Valor médio de pedido por cidade
media_por_cidade = inner_join.groupby('cidade')['valor'].mean().reset_index()
print("\n4. Valor médio de pedido por cidade:")
print(media_por_cidade)

# 5. Clientes sem pedidos
clientes_sem_pedidos = clientes[~clientes['id_cliente'].isin(pedidos['id_cliente'])]
print("\n5. Clientes sem pedidos:")
print(clientes_sem_pedidos)

# 6. Ranking de clientes por valor total
ranking = total_pedidos.sort_values(by='valor', ascending=False).reset_index(drop=True)
print("\n6. Ranking de clientes por valor total:")
print(ranking)