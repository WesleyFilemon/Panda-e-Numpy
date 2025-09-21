#Atividade 12: Análise de Correlação
#Objetivo: Calcular correlações e covariâncias.
# Dados de desempenho de estudantes
#np.random.seed(42)
#n_estudantes = 100

#estudantes_df = pd.DataFrame({
#'horas_estudo': np.random.normal(5, 2, n_estudantes),
#'horas_sono': np.random.normal(7, 1.5, n_estudantes),
#'nota_matematica': np.random.normal(75, 15, n_estudantes),
#'nota_portugues': np.random.normal(78, 12, n_estudantes),
#'frequencia': np.random.uniform(0.7, 1.0, n_estudantes)})

# TODO:
# 1. Calcular matriz de correlação
# 2. Encontrar a maior correlação positiva
# 3. Encontrar a maior correlação negativa
# 4. Calcular correlação entre horas de estudo e nota de matemática
# 5. Criar categorias de desempenho baseadas na nota média
# 6. Analisar se há correlação entre frequência e desempenho

import pandas as pd
import numpy as np


np.random.seed(42)
n_estudantes = 100

estudantes_df = pd.DataFrame({
    'horas_estudo': np.random.normal(5, 2, n_estudantes),
    'horas_sono': np.random.normal(7, 1.5, n_estudantes),
    'nota_matematica': np.random.normal(75, 15, n_estudantes),
    'nota_portugues': np.random.normal(78, 12, n_estudantes),
    'frequencia': np.random.uniform(0.7, 1.0, n_estudantes)
})

# 1. Matriz de correlação
correlacao = estudantes_df.corr()
print("\n1. Matriz de correlação:")
print(correlacao)

# 2. Maior correlação positiva (ignorando diagonal = 1.0)
cor_matrix = correlacao.unstack()
cor_matrix = cor_matrix[cor_matrix < 1]  # ignora diagonal
maior_pos = cor_matrix.idxmax(), cor_matrix.max()
print("\n2. Maior correlação positiva:", maior_pos)

# 3. Maior correlação negativa
maior_neg = cor_matrix.idxmin(), cor_matrix.min()
print("\n3. Maior correlação negativa:", maior_neg)

# 4. Correlação entre horas de estudo e nota de matemática
corr_estudo_matematica = estudantes_df['horas_estudo'].corr(estudantes_df['nota_matematica'])
print("\n4. Correlação (horas de estudo x nota de matemática):", corr_estudo_matematica)

# 5. Categorias de desempenho (baseado na média das notas)
estudantes_df['media_notas'] = estudantes_df[['nota_matematica','nota_portugues']].mean(axis=1)
estudantes_df['desempenho'] = pd.cut(estudantes_df['media_notas'],
                                     bins=[0, 60, 75, 90, 100],
                                     labels=['Baixo','Médio','Bom','Excelente'])
print("\n5. Amostra com categorias de desempenho:")
print(estudantes_df[['nota_matematica','nota_portugues','media_notas','desempenho']].head())

# 6. Correlação entre frequência e desempenho
corr_frequencia_media = estudantes_df['frequencia'].corr(estudantes_df['media_notas'])
print("\n6. Correlação entre frequência e desempenho (nota média):", corr_frequencia_media)