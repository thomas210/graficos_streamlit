import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import plotly.graph_objs as go
import plotly.express as px

st.title("Gráfico de Linha")

st.write("Utilizado principalmente para séries temporais, mostrando a evolução ao redor do tempo")

st.write("Exemplos")
st.write("Um gráfico de linhas que ilustra a variação da temperatura ao longo das estações do ano.")
st.write("Evolução das vendas durante um determinado período")
st.write("Etc...")

native, matplot, plotly = st.tabs(["Native Streamlit", "Matplotlib", "Plotly"])

# dados
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai']
temperaturas = [20, 22, 25, 23, 27]

# native
code = '''
import streamlit as st

meses = ['01_Jan', '02_Fev', '03_Mar', '04_Abr', '05_Mai']
temperaturas = [20, 22, 25, 23, 27]

data = {meses[i]: temperaturas[i] for i in range(len(meses))}
st.line_chart(data)
'''
native.code(code)

meses = ['01_Jan', '02_Fev', '03_Mar', '04_Abr', '05_Mai']

data = {meses[i]: temperaturas[i] for i in range(len(meses))}

native.line_chart(data)

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai']

# matplotlib
code = '''
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai']
temperaturas = [20, 22, 25, 23, 27]

plt.plot(meses, temperaturas)
plt.xlabel('Meses')
plt.ylabel('Temperaturas (°C)')
plt.title('Gráfico de Linhas')

st.pyplot(plt)
'''

matplot.code(code)

plt.plot(meses, temperaturas)
plt.xlabel('Meses')
plt.ylabel('Temperaturas (°C)')
plt.title('Gráfico de Linhas')

matplot.pyplot(plt)

# plotly

code = '''
import streamlit as st
import plotly.express as px

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai']
temperaturas = [20, 22, 25, 23, 27]

df = {'Meses': meses, 'Temperaturas': temperaturas}
fig = px.line(df, x='Meses', y='Temperaturas', title='Gráfico de Linhas - Plotly no Streamlit')

st.plotly_chart(fig)

'''

plotly.code(code)

df = {'Meses': meses, 'Temperaturas': temperaturas}
fig = px.line(df, x='Meses', y='Temperaturas', title='Gráfico de Linhas - Plotly no Streamlit')

plotly.plotly_chart(fig)