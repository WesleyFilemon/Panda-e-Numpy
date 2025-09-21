#Atividade 18: Amostragem e Aleatoriedade
#Objetivo: Praticar técnicas de amostragem.
# População de clientes
#np.random.seed(42)
#populacao_clientes = pd.DataFrame({
#'id': range(1, 10001),
#'idade': np.random.randint(18, 80, 10000),
#'renda': np.random.lognormal(10, 0.5, 10000),
#'regiao': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], 10000),
#'genero': np.random.choice(['M', 'F'], 10000)})

# TODO:
# 1. Extrair amostra aleatória de 100 clientes
# 2. Extrair amostra estratificada por região (25 de cada)
# 3. Comparar média de idade da amostra vs população
# 4. Fazer bootstrap: 10 amostras de 50 clientes cada
# 5. Calcular intervalo de confiança da renda média
# 6. Verificar se a amostra é representativa da população

import pandas as pd
import numpy as np

np.random.seed(42)

# População de clientes
populacao_clientes = pd.DataFrame({
    'id': range(1, 10001),
    'idade': np.random.randint(18, 80, 10000),
    'renda': np.random.lognormal(10, 0.5, 10000),
    'regiao': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], 10000),
    'genero': np.random.choice(['M', 'F'], 10000)
})

# 1. Amostra aleatória de 100 clientes
amostra_aleatoria = populacao_clientes.sample(100, random_state=42)
print("\n1. Amostra aleatória (primeiras 5 linhas):")
print(amostra_aleatoria.head())

# 2. Amostra estratificada por região (25 de cada) - corrigido
amostra_estratificada = (
    populacao_clientes
    .groupby('regiao', group_keys=False)
    .apply(lambda x: x.sample(25, random_state=42))
    .reset_index(drop=True)
)
print("\n2. Amostra estratificada por região:")
print(amostra_estratificada['regiao'].value_counts())

# 3. Comparar média de idade da amostra vs população
media_populacao = populacao_clientes['idade'].mean()
media_amostra = amostra_aleatoria['idade'].mean()
print(f"\n3. Média de idade - População: {media_populacao:.2f}, Amostra: {media_amostra:.2f}")

# 4. Bootstrap: 10 amostras de 50 clientes cada
bootstrap = [populacao_clientes.sample(50, replace=True, random_state=i) for i in range(10)]
medias_bootstrap = [b['renda'].mean() for b in bootstrap]
print("\n4. Médias de renda das 10 amostras bootstrap:")
print(medias_bootstrap)

# 5. Intervalo de confiança da renda média (95%)
media_renda = populacao_clientes['renda'].mean()
std_renda = populacao_clientes['renda'].std()
n = len(populacao_clientes)
ic_95 = (media_renda - 1.96*(std_renda/np.sqrt(n)), media_renda + 1.96*(std_renda/np.sqrt(n)))
print(f"\n5. Intervalo de confiança 95% da renda média: {ic_95}")

# 6. Verificar representatividade da amostra (comparando proporção por região)
prop_pop = populacao_clientes['regiao'].value_counts(normalize=True)
prop_amostra = amostra_aleatoria['regiao'].value_counts(normalize=True)
representatividade = pd.DataFrame({'População': prop_pop, 'Amostra': prop_amostra})
print("\n6. Representatividade da amostra por região:")
print(representatividade)
