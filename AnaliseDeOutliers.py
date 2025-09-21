#Atividade 16: Análise de Outliers
#Objetivo: Identificar e tratar valores atípicos.
# Dados de vendas com alguns outliers
#np.random.seed(42)
#vendas_outliers = pd.DataFrame({
#'vendedor': np.random.choice(['Ana', 'Bruno', 'Carlos'], 100),
#'valor_venda': np.concatenate([
#np.random.normal(1000, 200, 95), # Vendas normais
#np.array([5000, 4500, 6000, 4800, 5200]) # Outliers])})

# TODO:
# 1. Calcular quartis e IQR
# 2. Identificar outliers usando regra IQR (Q1 - 1.5*IQR, Q3 + 1.5*IQR)
# 3. Contar quantos outliers existem
# 4. Visualizar distribuição com describe()
# 5. Remover outliers e calcular nova média
# 6. Substituir outliers pela mediana

import pandas as pd
import numpy as np

np.random.seed(42)
vendas_outliers = pd.DataFrame({
    'vendedor': np.random.choice(['Ana', 'Bruno', 'Carlos'], 100),
    'valor_venda': np.concatenate([
        np.random.normal(1000, 200, 95),  # Vendas normais
        np.array([5000, 4500, 6000, 4800, 5200])  # Outliers
    ])
})

# 1. Calcular quartis e IQR
Q1 = vendas_outliers['valor_venda'].quantile(0.25)
Q3 = vendas_outliers['valor_venda'].quantile(0.75)
IQR = Q3 - Q1
print(f"\n1. Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")

# 2. Identificar outliers usando regra IQR
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR
outliers = vendas_outliers[(vendas_outliers['valor_venda'] < limite_inferior) | 
                           (vendas_outliers['valor_venda'] > limite_superior)]
print("\n2. Outliers identificados:")
print(outliers)

# 3. Contar quantos outliers existem
print("\n3. Quantidade de outliers:", len(outliers))

# 4. Visualizar distribuição com describe()
print("\n4. Estatísticas descritivas:")
print(vendas_outliers['valor_venda'].describe())

# 5. Remover outliers e calcular nova média
vendas_sem_outliers = vendas_outliers[~vendas_outliers.index.isin(outliers.index)]
nova_media = vendas_sem_outliers['valor_venda'].mean()
print("\n5. Média sem outliers:", nova_media)

# 6. Substituir outliers pela mediana
mediana = vendas_outliers['valor_venda'].median()
vendas_outliers['valor_venda_tratada'] = vendas_outliers['valor_venda'].apply(
    lambda x: mediana if x > limite_superior or x < limite_inferior else x
)
print("\n6. DataFrame com outliers substituídos pela mediana:")
print(vendas_outliers.head(10))
