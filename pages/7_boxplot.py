import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import plotly.express as px
import pandas as pd

st.title("Boxplot")

st.write("Sumariza a distribuição dos dados, mostrando quartis, mediana e outliers")

st.write("Exemplos")
st.write("Um diagrama de caixa que representa a distribuição de salários em diferentes departamentos de uma empresa.")
st.write("Distribuição de idades de passageiros")
st.write("Etc...")

native, matplot, plotly = st.tabs(["Native Streamlit", "Matplotlib", "Plotly"])

# dados
dados = [np.random.normal(0, std, 100) for std in range(1, 4)]

# native
native.error('Opa, não temos gráfico desse tipo')

# matplotlib
code = '''
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

dados = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(dados)
plt.xlabel('Distribuição')
plt.ylabel('Valores')
plt.title('Diagrama de Caixa')

st.pyplot(plt)
'''

matplot.code(code)

plt.boxplot(dados)
plt.xlabel('Distribuição')
plt.ylabel('Valores')
plt.title('Diagrama de Caixa')

matplot.pyplot(plt)

# plotly

code = '''
import streamlit as st
import plotly.express as px
import numpy as np

np.random.seed(0)
dados = [np.random.normal(0, std, 100) for std in range(1, 4)]

df = pd.DataFrame(dados).T

# Criando o boxplot com Plotly Express
fig = px.box(df.T, title='Diagrama de Caixa - Plotly no Streamlit')

plotly.plotly_chart(fig)


st.plotly_chart(fig)
'''

plotly.code(code)

df = pd.DataFrame(dados).T

# Criando o boxplot com Plotly Express
fig = px.box(df.T, title='Diagrama de Caixa - Plotly no Streamlit')

plotly.plotly_chart(fig)