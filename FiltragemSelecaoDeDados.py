#Atividade 5: Filtragem e Seleção de Dados
#Objetivo: Praticar seleção condicional em DataFrames.
# Criar DataFrame de vendas
#np.random.seed(42)
#vendas_df = pd.DataFrame({
#'produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Headset'] * 20,
#'vendedor': np.random.choice(['Ana', 'Bruno', 'Carlos'], 100),
#'valor': np.random.uniform(50, 1000, 100),
#'quantidade': np.random.randint(1, 10, 100)})

import numpy as np
import pandas as pd

# TODO:
# 1. Filtrar vendas com valor > 500
# 2. Mostrar apenas vendas do vendedor 'Ana'
# 3. Filtrar produtos 'Notebook' OU 'Monitor'
# 4. Vendas com valor entre 200 e 600
# 5. Top 10 maiores vendas por valor
# 6. Vendas do 'Bruno' de produtos 'Mouse' ou 'Teclado'

np.random.seed(42)
vendas_df = pd.DataFrame({
'produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Headset'] * 20,
'vendedor': np.random.choice(['Ana', 'Bruno', 'Carlos'], 100),
'valor': np.random.uniform(50, 1000, 100),
'quantidade': np.random.randint(1, 10, 100)})

# 1. Filtrar vendas com valor > 500
vendas_maiores_500 = vendas_df[vendas_df['valor'] > 500]
print("Vendas com valor > 500:")
print(vendas_maiores_500)

# 2. Mostrar apenas vendas do vendedor 'Ana'
vendas_ana = vendas_df[vendas_df['vendedor'] == 'Ana']
print("\nVendas do vendedor Ana:")
print(vendas_ana)

# 3. Filtrar produtos 'Notebook' OU 'Monitor'
vendas_notebook_monitor = vendas_df[vendas_df['produto'].isin(['Notebook', 'Monitor'])]
print("\nVendas de produtos Notebook ou Monitor:")
print(vendas_notebook_monitor)

# 4. Vendas com valor entre 200 e 600
vendas_200_600 = vendas_df[(vendas_df['valor'] >= 200) & (vendas_df['valor'] <= 600)]
print("\nVendas com valor entre 200 e 600:")
print(vendas_200_600)

# 5. Top 10 maiores vendas por valor
top10_vendas = vendas_df.nlargest(10, 'valor')
print("\nTop 10 maiores vendas por valor:")
print(top10_vendas)

# 6. Vendas do 'Bruno' de produtos 'Mouse' ou 'Teclado'
vendas_bruno_mouse_teclado = vendas_df[
    (vendas_df['vendedor'] == 'Bruno') &
    (vendas_df['produto'].isin(['Mouse', 'Teclado']))
]
print("\nVendas do Bruno de Mouse ou Teclado:")
print(vendas_bruno_mouse_teclado)