# Atividade 13: Aplicação de Funções
#Objetivo: Usar apply, map e transform.
# Dados de funcionários
#funcionarios_df = pd.DataFrame({
#'nome': ['Ana Silva', 'Bruno Santos', 'Carlos Lima', 'Diana Costa'],
#'email': ['ana.silva@email.com', 'bruno.santos@email.com',
#'carlos.lima@email.com', 'diana.costa@email.com'],
#'salario': [3500, 4200, 5500, 3800],
#'data_admissao': ['2020-01-15', '2019-03-22', '2018-07-10', '2021-05-30']})

# TODO:
# 1. Extrair apenas o primeiro nome de cada funcionário
# 2. Criar uma função para classificar salários: Alto (>5000), Médio (3000-5000), Baixo (<3000)
# 3. Converter data_admissao para datetime
# 4. Calcular quantos anos cada funcionário trabalha na empresa
# 5. Criar um domínio de email padronizado (@empresa.com)
# 6. Aplicar aumento de 10% nos salários menores que 4000

import pandas as pd
from datetime import datetime


funcionarios_df = pd.DataFrame({
    'nome': ['Ana Silva', 'Bruno Santos', 'Carlos Lima', 'Diana Costa'],
    'email': ['ana.silva@email.com', 'bruno.santos@email.com',
              'carlos.lima@email.com', 'diana.costa@email.com'],
    'salario': [3500, 4200, 5500, 3800],
    'data_admissao': ['2020-01-15', '2019-03-22', '2018-07-10', '2021-05-30']
})

# 1. Extrair apenas o primeiro nome
funcionarios_df['primeiro_nome'] = funcionarios_df['nome'].str.split().str[0]

# 2. Classificar salários
def classificar_salario(sal):
    if sal > 5000:
        return 'Alto'
    elif sal >= 3000:
        return 'Médio'
    else:
        return 'Baixo'

funcionarios_df['categoria_salario'] = funcionarios_df['salario'].apply(classificar_salario)

# 3. Converter data_admissao para datetime
funcionarios_df['data_admissao'] = pd.to_datetime(funcionarios_df['data_admissao'])

# 4. Calcular quantos anos de empresa
hoje = pd.Timestamp.today()
funcionarios_df['anos_empresa'] = funcionarios_df['data_admissao'].apply(lambda d: round((hoje - d).days / 365, 1))

# 5. Criar domínio de email padronizado (@empresa.com)
funcionarios_df['email_padronizado'] = funcionarios_df['primeiro_nome'].str.lower() + "@empresa.com"

# 6. Aumento de 10% para salários menores que 4000
funcionarios_df['salario'] = funcionarios_df['salario'].astype(float)

funcionarios_df.loc[funcionarios_df['salario'] < 4000, 'salario'] *= 1.10

print(funcionarios_df)