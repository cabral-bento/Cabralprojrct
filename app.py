import pandas as pd
import plotly.express as px
import streamlit as st
        
# Lendo os dados do CSV
car_data = pd.read_csv('vehicles.csv')

# Caixa de seleção para o histograma
show_hist = st.checkbox('Mostrar histograma')

# Caixa de seleção para o gráfico de dispersão
show_scatter = st.checkbox('Mostrar gráfico de dispersão')

# Se a caixa de seleção do histograma for marcada
if show_hist:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # Criar o histograma
    fig_hist = px.histogram(car_data, x="odometer")
    
    # Exibir o gráfico de histograma
    st.plotly_chart(fig_hist, use_container_width=True)

# Se a caixa de seleção do gráfico de dispersão for marcada
if show_scatter:
    st.write('Criando um gráfico de dispersão com base nos dados de preço e quilometragem')
    
    # Criar o gráfico de dispersão
    fig_scatter = px.scatter(car_data, x='odometer', y='price', title="Preço vs Odômetro")
    
    # Exibir o gráfico de dispersão
    st.plotly_chart(fig_scatter, use_container_width=True)