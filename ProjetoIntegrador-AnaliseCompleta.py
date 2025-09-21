#Atividade 20: Projeto Integrador - Análise Completa
#Objetivo: Combinar todos os conceitos em um projeto real.
# Simular dados de e-commerce
#np.random.seed(42)

# Gerar dados sintéticos de e-commerce
#clientes = pd.DataFrame({
#'id_cliente': range(1, 1001),
#'nome': [f'Cliente_{i}' for i in range(1, 1001)],
#'idade': np.random.randint(18, 70, 1000),
#'cidade': np.random.choice(['SP', 'RJ', 'MG', 'RS', 'PR'], 1000),
#'data_cadastro': pd.date_range('2022-01-01', periods=1000, freq='D')})

#produtos = pd.DataFrame({
#'id_produto': range(1, 101),
#'categoria': np.random.choice(['Eletrônicos', 'Roupas', 'Casa', 'Livros'], 100),
#'preco': np.random.uniform(10, 500, 100)})

#vendas = pd.DataFrame({
#'id_venda': range(1, 5001),
#'id_cliente': np.random.randint(1, 1001, 5000),
#'id_produto': np.random.randint(1, 101, 5000),
#'quantidade': np.random.randint(1, 5, 5000),
#'data_venda': pd.date_range('2022-01-01', periods=5000, freq='H')})

# DESAFIO COMPLETO:
# 1. Integrar as três tabelas em um dataset completo
# 2. Calcular receita total por mês
# 3. Identificar top 10 clientes por valor total
# 4. Analisar sazonalidade das vendas
# 5. Calcular ticket médio por categoria
# 6. Identificar produtos com baixo giro
# 7. Segmentar clientes por comportamento de compra
# 8. Calcular taxa de retenção mensal
# 9. Criar dashboard de métricas principais
# 10. Gerar insights e recomendações de negócio

import pandas as pd
import numpy as np

np.random.seed(42)

# -----------------------------
# 1. Criar os datasets sintéticos
# -----------------------------
clientes = pd.DataFrame({
    'id_cliente': range(1, 1001),
    'nome': [f'Cliente_{i}' for i in range(1, 1001)],
    'idade': np.random.randint(18, 70, 1000),
    'cidade': np.random.choice(['SP', 'RJ', 'MG', 'RS', 'PR'], 1000),
    'data_cadastro': pd.date_range('2022-01-01', periods=1000, freq='D')
})

produtos = pd.DataFrame({
    'id_produto': range(1, 101),
    'categoria': np.random.choice(['Eletrônicos', 'Roupas', 'Casa', 'Livros'], 100),
    'preco': np.random.uniform(10, 500, 100)
})

vendas = pd.DataFrame({
    'id_venda': range(1, 5001),
    'id_cliente': np.random.randint(1, 1001, 5000),
    'id_produto': np.random.randint(1, 101, 5000),
    'quantidade': np.random.randint(1, 5, 5000),
    'data_venda': pd.date_range('2022-01-01', periods=5000, freq='H')
})

# -----------------------------
# 1. Integrar as três tabelas
# -----------------------------
df = vendas.merge(clientes, on='id_cliente').merge(produtos, on='id_produto')
df['receita'] = df['quantidade'] * df['preco']

# -----------------------------
# 2. Receita total por mês
# -----------------------------
df['mes'] = df['data_venda'].dt.to_period('M')
receita_mensal = df.groupby('mes')['receita'].sum()
print("\nReceita total por mês:")
print(receita_mensal)

# -----------------------------
# 3. Top 10 clientes por valor total
# -----------------------------
top_clientes = df.groupby('nome')['receita'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 clientes por receita:")
print(top_clientes)

# -----------------------------
# 4. Sazonalidade das vendas (por hora do dia)
# -----------------------------
df['hora'] = df['data_venda'].dt.hour
vendas_horario = df.groupby('hora')['quantidade'].sum()
print("\nVendas por hora do dia:")
print(vendas_horario)

# -----------------------------
# 5. Ticket médio por categoria
# -----------------------------
ticket_medio = df.groupby('categoria')['receita'].mean()
print("\nTicket médio por categoria:")
print(ticket_medio)

# -----------------------------
# 6. Produtos com baixo giro (quantidade vendida total)
# -----------------------------
produtos_giro = df.groupby('id_produto')['quantidade'].sum()
baixo_giro = produtos_giro.nsmallest(10)
print("\nProdutos com baixo giro:")
print(baixo_giro)

# -----------------------------
# 7. Segmentação de clientes por comportamento
# -----------------------------
df_clientes = df.groupby('id_cliente').agg({
    'receita': 'sum',
    'id_venda': 'count',
    'quantidade': 'sum'
}).rename(columns={'id_venda':'num_pedidos', 'quantidade':'total_itens'})

# Segmentação simples
df_clientes['segmento'] = pd.qcut(df_clientes['receita'], 4, labels=['Bronze', 'Prata', 'Ouro', 'Platina'])
print("\nSegmentos de clientes:")
print(df_clientes['segmento'].value_counts())

# -----------------------------
# 8. Taxa de retenção mensal
# -----------------------------
# Clientes ativos por mês
clientes_ativos = df.groupby('mes')['id_cliente'].nunique()
taxa_retentao = clientes_ativos.pct_change().fillna(0)
print("\nTaxa de retenção mensal (%):")
print(taxa_retentao * 100)

# -----------------------------
# 9. Dashboard de métricas principais
# -----------------------------
dashboard = pd.DataFrame({
    'Receita Mensal': receita_mensal,
    'Clientes Ativos': clientes_ativos,
    'Taxa Retenção (%)': taxa_retentao * 100
})
print("\nDashboard:")
print(dashboard)

# -----------------------------
# 10. Insights e recomendações
# -----------------------------
# Exemplos simples de insights
insights = {
    'Categorias mais lucrativas': ticket_medio.sort_values(ascending=False).index.tolist(),
    'Horas de pico de vendas': vendas_horario.sort_values(ascending=False).head(3).index.tolist(),
    'Segmentos mais valiosos': df_clientes.groupby('segmento')['receita'].sum().sort_values(ascending=False).index.tolist(),
    'Produtos a reavaliar estoque': baixo_giro.index.tolist()
}
print("\nInsights e recomendações:")
for k,v in insights.items():
    print(f"{k}: {v}")
