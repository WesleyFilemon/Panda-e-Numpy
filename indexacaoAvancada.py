#Atividade 14: Indexação Avançada
#Objetivo: Trabalhar com MultiIndex e indexação complexa.
# Dados de vendas por loja, produto e mês
#vendas_multi = pd.DataFrame({
#'loja': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'] * 4,
#'produto': ['X', 'Y', 'Z'] * 12,
#'mes': ['Jan', 'Jan', 'Jan', 'Jan', 'Jan', 'Jan', 'Jan', 'Jan', 'Jan',
#'Fev', 'Fev', 'Fev', 'Fev', 'Fev', 'Fev', 'Fev', 'Fev', 'Fev',
#'Mar', 'Mar', 'Mar', 'Mar', 'Mar', 'Mar', 'Mar', 'Mar', 'Mar',
#'Abr', 'Abr', 'Abr', 'Abr', 'Abr', 'Abr', 'Abr', 'Abr', 'Abr'],
#'vendas': np.random.randint(50, 200, 36)})

# TODO:
# 1. Criar MultiIndex com loja e produto
# 2. Selecionar vendas da loja 'A'
# 3. Selecionar vendas do produto 'X' em todas as lojas
# 4. Calcular total de vendas por loja
# 5. Encontrar o produto mais vendido em cada loja
# 6. Criar tabela pivot com lojas vs produtos

import pandas as pd
import numpy as np

vendas_multi = pd.DataFrame({
    'loja': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'] * 4,
    'produto': ['X', 'Y', 'Z'] * 12,
    'mes': ['Jan'] * 9 + ['Fev'] * 9 + ['Mar'] * 9 + ['Abr'] * 9,
    'vendas': np.random.randint(50, 200, 36)
})

# 1. Criar MultiIndex com loja e produto
vendas_multi = vendas_multi.set_index(['loja', 'produto'])
print("\nDataFrame com MultiIndex:")
print(vendas_multi.head())

# 2. Selecionar vendas da loja 'A'
print("\nVendas da loja A:")
print(vendas_multi.loc['A'])

# 3. Selecionar vendas do produto 'X' em todas as lojas
print("\nVendas do produto X em todas as lojas:")
print(vendas_multi.xs('X', level='produto'))

# 4. Calcular total de vendas por loja
print("\nTotal de vendas por loja:")
print(vendas_multi.groupby('loja')['vendas'].sum())

# 5. Encontrar o produto mais vendido em cada loja
print("\nProduto mais vendido em cada loja:")
print(vendas_multi.groupby(['loja', 'produto'])['vendas'].sum()
      .groupby('loja').idxmax())

# 6. Criar tabela pivot com lojas vs produtos
pivot = vendas_multi.reset_index().pivot_table(
    index='loja', columns='produto', values='vendas', aggfunc='sum'
)
print("\nTabela pivot (lojas vs produtos):")
print(pivot)
