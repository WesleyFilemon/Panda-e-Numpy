# Atividade 2: Operações Aritméticas com Series
#Objetivo: Praticar operações matemáticas entre Series.
# Dados de duas lojas
#loja_a = pd.Series([100, 150, 200, 120, 180],
#index=['Jan', 'Fev', 'Mar', 'Abr', 'Mai'])
#loja_b = pd.Series([80, 200, 150, 100, 220],
#index=['Jan', 'Fev', 'Mar', 'Abr', 'Mai'])

# TODO:
# 1. Calcular a soma das vendas de ambas as lojas
# 2. Calcular a diferença (Loja A - Loja B)
# 3. Calcular o produto das vendas
# 4. Dividir vendas da Loja A pelas da Loja B
# 5. Aplicar um desconto de 10% em todas as vendas da Loja A
# 6. Encontrar em quais meses a Loja A vendeu mais que a Loja B

import numpy as np
import pandas as pd

loja_a = pd.Series([100, 150, 200, 120, 180],
index=['Jan', 'Fev', 'Mar', 'Abr', 'Mai'])
loja_b = pd.Series([80, 200, 150, 100, 220],
index=['Jan', 'Fev', 'Mar', 'Abr', 'Mai'])

# 1. Calcular a soma das vendas de ambas as lojas
vendas_totais = loja_a + loja_b
print("Soma das vendas mês a mês:")
print(vendas_totais)


soma_total = vendas_totais.sum()
print("\nSoma total das vendas das duas lojas:", soma_total)

# 2. Calcular a diferença (Loja A - Loja B)

Diferenca = loja_a - loja_b
print("Diferença (loja_a - loja_b): ")
print(Diferenca)

# 3. Calcular o produto das vendas
produto_vendas = loja_a * loja_b
print("Produto das vendas (Loja A x Loja B) mês a mês:")
print(produto_vendas)

# 4. Dividir vendas da Loja A pelas da Loja B
produto_vendas = loja_a / loja_b
print("Divisão das vendas (Loja A / Loja B) mês a mês:")
print(round(produto_vendas,2))

# 5. Aplicar um desconto de 10% em todas as vendas da Loja A
loja_a_desconto = loja_a * 0.9

print("Vendas da Loja A com desconto de 10%:")
print(loja_a_desconto)

# 6. Encontrar meses em que Loja A vendeu mais que Loja B
meses_maior = loja_a[loja_a > loja_b]
print("Meses em que Loja A vendeu mais que Loja B:")
print(meses_maior)