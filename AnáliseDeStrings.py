#Atividade 15: Análise de Strings
#Objetivo: Manipular dados de texto com Pandas.
# Dados de produtos com descrições
#produtos_df = pd.DataFrame({
#'codigo': ['PROD001', 'PROD002', 'PROD003', 'PROD004', 'PROD005'],
#'descricao': ['Notebook Dell 15.6" Intel i7',
#'Mouse Wireless Logitech M705',
#'Teclado Mecânico RGB Gamer',
#'Monitor LG 24" Full HD',
#'Headset Sony WH-1000XM4'],
#'categoria': ['informatica', 'PERIFERICOS', 'Periféricos', 'informatica', 'Audio']})

# TODO:
# 1. Padronizar categoria (todas minúsculas)
# 2. Extrair a marca de cada produto (primeira palavra da descrição)
# 3. Verificar quais produtos contêm "RGB" na descrição
# 4. Contar caracteres na descrição
# 5. Criar código simplificado (primeiras 4 letras + últimos 3 números)
# 6. Separar descrição em colunas: marca, modelo, especificações

import pandas as pd


produtos_df = pd.DataFrame({
    'codigo': ['PROD001', 'PROD002', 'PROD003', 'PROD004', 'PROD005'],
    'descricao': [
        'Notebook Dell 15.6" Intel i7',
        'Mouse Wireless Logitech M705',
        'Teclado Mecânico RGB Gamer',
        'Monitor LG 24" Full HD',
        'Headset Sony WH-1000XM4'
    ],
    'categoria': ['informatica', 'PERIFERICOS', 'Periféricos', 'informatica', 'Audio']
})

# 1. Padronizar categoria (todas minúsculas)
produtos_df['categoria'] = produtos_df['categoria'].str.lower()

# 2. Extrair a marca (primeira palavra da descrição)
produtos_df['marca'] = produtos_df['descricao'].str.split().str[0]

# 3. Verificar produtos que contêm "RGB"
produtos_df['tem_RGB'] = produtos_df['descricao'].str.contains("RGB", case=False)

# 4. Contar caracteres na descrição
produtos_df['tam_descricao'] = produtos_df['descricao'].str.len()

# 5. Criar código simplificado (primeiras 4 letras do código + últimos 3 números)
produtos_df['codigo_simpl'] = produtos_df['codigo'].str[:4] + produtos_df['codigo'].str[-3:]

# 6. Separar descrição em colunas: marca, modelo, especificações
# Vamos considerar: marca = primeira palavra, modelo = segunda palavra, resto = especificações
descricao_split = produtos_df['descricao'].str.split(n=2, expand=True)
produtos_df['marca'] = descricao_split[0]
produtos_df['modelo'] = descricao_split[1]
produtos_df['especificacoes'] = descricao_split[2]

print(produtos_df)
