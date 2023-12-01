import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

    st.dataframe(data)

    st.subheader('Informações Gerais')
    st.write(data.describe())

    st.subheader('Distribuição de Sobreviventes')
    surv_counts = data['Survived'].value_counts()
    st.bar_chart(surv_counts)

# Análise por Classe
elif menu == 'Análise por Classe':
    st.header('Análise por Classe')

    st.subheader('Contagem de Passageiros por Classe')
    class_counts = data['Pclass'].value_counts()
    st.bar_chart(class_counts)

    st.subheader('Taxa de Sobrevivência por Classe')
    class_survival = data.groupby('Pclass')['Survived'].mean()
    st.bar_chart(class_survival)

# Análise por Idade
elif menu == 'Análise por Idade':
    st.header('Análise por Idade')

    st.subheader('Distribuição de Idades')
    # st.bar_chart(data['Age'].dropna(), bins=20, edgecolor='black')
    # st.pyplot()

    st.subheader('Distribuição de Idades por Classe')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Pclass', y='Age', data=data)
    st.pyplot()

# Créditos
st.sidebar.text("Desenvolvido por: Nova Roma")