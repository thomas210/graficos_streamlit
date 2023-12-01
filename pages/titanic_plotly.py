import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# Carregar os dados
@st.cache_data
def load_data():
    data = pd.read_csv('titanic.csv')
    return data

data = load_data()

# Título do Dashboard
st.title('Dashboard do Titanic')

# Sidebar com opções
st.sidebar.title('Opções')
menu = st.sidebar.selectbox('Selecione uma opção:', ('Visão Geral', 'Análise por Classe', 'Análise por Idade'))

# Visão Geral dos Dados
if menu == 'Visão Geral':
    st.header('Visão Geral dos Passageiros')
    st.write(data.head())

    st.subheader('Informações Gerais')
    st.write(data.describe())

    st.subheader('Distribuição de Sobreviventes')
    surv_counts = data['Survived'].value_counts()
    fig_surv_counts = px.bar(x=surv_counts.index, y=surv_counts.values, labels={'x': 'Sobreviveu', 'y': 'Contagem'})
    st.plotly_chart(fig_surv_counts)

# Análise por Classe
elif menu == 'Análise por Classe':
    st.header('Análise por Classe')

    st.subheader('Contagem de Passageiros por Classe')
    class_counts = data['Pclass'].value_counts().sort_index()
    fig_class_counts = px.bar(x=class_counts.index, y=class_counts.values, labels={'x': 'Classe', 'y': 'Contagem'})
    st.plotly_chart(fig_class_counts)

    st.subheader('Taxa de Sobrevivência por Classe')
    class_survival = data.groupby('Pclass')['Survived'].mean().reset_index()
    fig_class_survival = px.bar(class_survival, x='Pclass', y='Survived', labels={'x': 'Classe', 'y': 'Taxa de Sobrevivência'})
    st.plotly_chart(fig_class_survival)

# Análise por Idade
elif menu == 'Análise por Idade':
    st.header('Análise por Idade')

    st.subheader('Distribuição de Idades')
    fig_age_distribution = px.histogram(data.dropna(), x='Age', nbins=20, labels={'x': 'Idade'}, marginal='box')
    st.plotly_chart(fig_age_distribution)

    st.subheader('Distribuição de Idades por Classe')
    fig_age_by_class = px.box(data.dropna(), x='Pclass', y='Age', labels={'x': 'Classe', 'y': 'Idade'})
    st.plotly_chart(fig_age_by_class)

# Créditos
st.sidebar.text("Desenvolvido por: Seu Nome")
