#Atividade 3: Estatísticas Descritivas com Series
#Objetivo: Calcular estatísticas básicas de um conjunto de dados.
# Notas de uma turma
#notas = pd.Series([7.5, 8.0, 6.5, 9.0, 7.0, 8.5, 6.0, 9.5, 7.8, 8.2])

# TODO:
# 1. Calcular média, mediana e desvio padrão
# 2. Encontrar a nota máxima e mínima
# 3. Contar quantos alunos tiraram nota >= 8.0
# 4. Criar uma nova Series com as notas normalizadas (0-10 para 0-1)
# 5. Classificar as notas em categorias: A(>=9), B(8-8.9), C(7-7.9), D(<7)

import numpy as np
import pandas as pd

notas = pd.Series([7.5, 8.0, 6.5, 9.0, 7.0, 8.5, 6.0, 9.5, 7.8, 8.2])

# 1. Calcular média, mediana e desvio padrão
media = notas.mean()
mediana = notas.median()
desvio_padrao = notas.std()

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desvio padrão: {desvio_padrao:.2f}")

# 2. Encontrar a nota máxima e mínima

nota_maxima = notas.max()
nota_minima = notas.min()

print(f"Nota máxima: {nota_maxima}")
print(f"Nota mínima: {nota_minima}")

# 3. Contar quantos alunos tiraram nota >= 8.0
alunos_acima_8 = (notas >= 8.0).sum()

print(f"Número de alunos com nota >= 8.0: {alunos_acima_8}")

# 4. Criar uma nova Series com as notas normalizadas (0-10 para 0-1)
notas_normalizadas = notas / 10

print("Notas normalizadas (0-1):")
print(notas_normalizadas)

# 5. Classificar as notas em categorias: A(>=9), B(8-8.9), C(7-7.9), D(<7)
def categoria(nota):
    if nota >= 9:
        return 'A'
    elif 8 <= nota < 9:
        return 'B'
    elif 7 <= nota < 8:
        return 'C'
    else:
        return 'D'

notas_categoria = notas.apply(categoria)

print("Notas com categorias:")
print(notas_categoria)