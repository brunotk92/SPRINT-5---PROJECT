import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo os dados
car_data = pd.read_csv('vehicles.csv') 

# PASSO 2: Adicionando um cabeçalho
st.header('Análise de Dados de Anúncios de Veículos')

# Seção do Histogram
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Seção do Gráfico de Dispersão (Scatter Plot)
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão para o preço vs odômetro')
    # Criando o gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # Exibindo o gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)