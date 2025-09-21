#Atividade 6: Agrupamento e Agregação
#Objetivo: Usar groupby para análises agregadas.
# Usar o DataFrame da atividade anterior (vendas_df)

import numpy as np
import pandas as pd

# TODO:
# 1. Calcular total de vendas por vendedor
# 2. Média de valor por produto
# 3. Quantidade total vendida por produto
# 4. Maior venda de cada vendedor
# 5. Contar quantas vendas cada vendedor fez
# 6. Criar uma tabela pivot: vendedor vs produto (soma dos valores)


vendas_df = pd.DataFrame({
'produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Headset'] * 20,
'vendedor': np.random.choice(['Ana', 'Bruno', 'Carlos'], 100),
'valor': np.random.uniform(50, 1000, 100),
'quantidade': np.random.randint(1, 10, 100)})

# 1. Total de vendas por vendedor
total_vendas_vendedor = vendas_df.groupby('vendedor')['valor'].sum()
print("Total de vendas por vendedor:")
print(total_vendas_vendedor)

# 2. Média de valor por produto
media_valor_produto = vendas_df.groupby('produto')['valor'].mean()
print("\nMédia de valor por produto:")
print(media_valor_produto)

# 3. Quantidade total vendida por produto
quantidade_total_produto = vendas_df.groupby('produto')['quantidade'].sum()
print("\nQuantidade total vendida por produto:")
print(quantidade_total_produto)

# 4. Maior venda de cada vendedor
maior_venda_vendedor = vendas_df.groupby('vendedor')['valor'].max()
print("\nMaior venda de cada vendedor:")
print(maior_venda_vendedor)

# 5. Contar quantas vendas cada vendedor fez
contagem_vendas_vendedor = vendas_df.groupby('vendedor')['valor'].count()
print("\nNúmero de vendas de cada vendedor:")
print(contagem_vendas_vendedor)

# 6. Criar uma tabela pivot: vendedor vs produto (soma dos valores)
tabela_pivot = vendas_df.pivot_table(values='valor', index='vendedor', columns='produto', aggfunc='sum', fill_value=0)
print("\nTabela pivot (vendedor vs produto, soma dos valores):")
print(tabela_pivot)
