import streamlit as st
import pandas as pd
import sqlite3

# Conectar com o banco de dados
conn = sqlite3.connect('../data/quotes.db')

# Carregar os dados do banco de dados em um DataFrame
df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

# Fechar a conexão com o banco de dados
conn.close()

# Título da página
st.title('Análise das Ofertas do Mercado Livre')

# Adicionar os KPIs
st.subheader('KPIs principais do sistema!')
col1, col2, col3 = st.columns(3)

# KPI 1 - Número total de itens
total_itens = df.shape[0]
col1.metric(label="Número de Itens", value=total_itens)

# KPI 2 - Preço médio new
average_new_price = df['new_price'].mean()
col2.metric(label="Preço médio novo em (R$)", value=f"{average_new_price:.2f}")

# KPI 3 - Preço médio old
average_old_price = df['old_price'].mean()
col3.metric(label="Preço Médio Antigo em (R$)", value=f"{average_old_price:.2f}")