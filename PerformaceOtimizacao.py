#Atividade 19: Performance e Otimização
#Objetivo: Comparar performance de diferentes operações.
#import time

# Criar DataFrame grande
#np.random.seed(42)
#df_grande = pd.DataFrame({
#'A': np.random.randn(100000),
#'B': np.random.randn(100000),
#'C': np.random.choice(['X', 'Y', 'Z'], 100000),
#'D': np.random.randint(1, 1000, 100000)})

# TODO:
# 1. Comparar tempo: loop vs operação vetorizada para calcular A + B
# 2. Comparar apply vs operação direta para classificar valores de A
# 3. Testar performance de query() vs indexação booleana
# 4. Comparar groupby vs pivot para agregações
# 5. Medir tempo de diferentes métodos de ordenação
# 6. Avaliar uso de memória com memory_usage()

import pandas as pd
import numpy as np
import time

np.random.seed(42)
df_grande = pd.DataFrame({
    'A': np.random.randn(100000),
    'B': np.random.randn(100000),
    'C': np.random.choice(['X', 'Y', 'Z'], 100000),
    'D': np.random.randint(1, 1000, 100000)
})

# 1. Comparar tempo: loop vs vetorizado para calcular A + B
start = time.time()
soma_loop = []
for i in range(len(df_grande)):
    soma_loop.append(df_grande['A'].iloc[i] + df_grande['B'].iloc[i])
tempo_loop = time.time() - start

start = time.time()
soma_vetor = df_grande['A'] + df_grande['B']
tempo_vetor = time.time() - start

print(f"1. Tempo loop: {tempo_loop:.4f}s, Tempo vetorizado: {tempo_vetor:.4f}s")

# 2. Comparar apply vs operação direta para classificar valores de A
def classifica(valor):
    if valor > 1:
        return 'Alto'
    elif valor < -1:
        return 'Baixo'
    else:
        return 'Médio'

start = time.time()
df_grande['classe_apply'] = df_grande['A'].apply(classifica)
tempo_apply = time.time() - start

start = time.time()
df_grande['classe_vetor'] = np.where(df_grande['A'] > 1, 'Alto', np.where(df_grande['A'] < -1, 'Baixo', 'Médio'))
tempo_vetor_class = time.time() - start

print(f"2. Tempo apply: {tempo_apply:.4f}s, Tempo vetorizado: {tempo_vetor_class:.4f}s")

# 3. Testar performance query() vs indexação booleana
start = time.time()
resultado_query = df_grande.query("C == 'X' & D > 500")
tempo_query = time.time() - start

start = time.time()
resultado_bool = df_grande[(df_grande['C'] == 'X') & (df_grande['D'] > 500)]
tempo_bool = time.time() - start

print(f"3. Tempo query(): {tempo_query:.4f}s, Tempo boolean indexing: {tempo_bool:.4f}s")

# 4. Comparar groupby vs pivot para agregações
start = time.time()
agregado_groupby = df_grande.groupby('C')['D'].sum()
tempo_groupby = time.time() - start

start = time.time()
agregado_pivot = df_grande.pivot_table(index='C', values='D', aggfunc='sum')
tempo_pivot = time.time() - start

print(f"4. Tempo groupby: {tempo_groupby:.4f}s, Tempo pivot_table: {tempo_pivot:.4f}s")

# 5. Medir tempo de diferentes métodos de ordenação
start = time.time()
df_grande.sort_values('A', inplace=True)
tempo_sort = time.time() - start

start = time.time()
df_grande.sort_values(['C', 'D'], inplace=True)
tempo_sort_multi = time.time() - start

print(f"5. Tempo sort A: {tempo_sort:.4f}s, Tempo sort C+D: {tempo_sort_multi:.4f}s")

# 6. Avaliar uso de memória
uso_memoria = df_grande.memory_usage(deep=True)
print("\n6. Uso de memória por coluna (bytes):")
print(uso_memoria)
print(f"Uso total de memória: {uso_memoria.sum()/1024**2:.2f} MB")
