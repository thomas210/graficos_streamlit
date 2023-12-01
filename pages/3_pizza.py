import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import plotly.graph_objs as go
import plotly.express as px

st.title("Gráfico de Pizza")

st.write("Destaca as partes de um todo, mostrando as proporções.")

st.write("Exemplos")
st.write("Distribuição percentual de gastos em diferentes categorias")
st.write("Distribuição de votos entre diferentes grupos de idade")
st.write("Distribuição de peso entre diferentes categorias de produtos")
st.write("Etc...")

native, matplot, plotly = st.tabs(["Native Streamlit", "Matplotlib", "Plotly"])

# dados
categorias = ['Alimentação', 'Moradia', 'Transporte', 'Outros']
gastos = [30, 35, 20, 15]

# native
native.error('Opa, não temos gráfico desse tipo')

# matplotlib
code = '''
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

categorias = ['Alimentação', 'Moradia', 'Transporte', 'Outros']
gastos = [30, 35, 20, 15]

plt.pie(gastos, labels=categorias, autopct='%1.1f%%')
plt.title('Gráfico de Pizza')

st.pyplot(plt)
'''

matplot.code(code)

plt.pie(gastos, labels=categorias, autopct='%1.1f%%')
plt.title('Gráfico de Pizza')

matplot.pyplot(plt)

# plotly

code = '''
import streamlit as st
import plotly.express as px

categorias = ['Alimentação', 'Moradia', 'Transporte', 'Outros']
gastos = [30, 35, 20, 15]

fig = px.pie(values=gastos, names=categorias, title='Gráfico de Pizza - Plotly no Streamlit')
st.plotly_chart(fig)
'''

plotly.code(code)

fig = px.pie(values=gastos, names=categorias, title='Gráfico de Pizza - Plotly no Streamlit')

plotly.plotly_chart(fig)