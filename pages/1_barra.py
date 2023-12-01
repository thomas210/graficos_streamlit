import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import plotly.graph_objs as go

st.title("Gráfico de Barras")

st.write("Exemplo mais comum de tipo de gráficos, usado mais comumente para analisar diferentes categorias ou diferentes períodos de tempo")

st.write("Exemplos")
st.write("Um gráfico de barras que mostra as vendas mensais de uma empresa ao longo de um ano.")
st.write("Um gráfico para analisare a quantidade de jogadores em cada servidor")
st.write("Quantidade de Funcionários por cargo")
st.write("Etc...")

native, matplot, plotly = st.tabs(["Native Streamlit", "Matplotlib", "Plotly"])

# dados
categorias = ['A', 'B', 'C', 'D']
valores = [25, 40, 30, 35]

# native
code = '''
import streamlit as st

categorias = ['A', 'B', 'C', 'D']
valores = [25, 40, 30, 35]

st.bar_chart(dict(zip(categorias, valores)))
'''
native.code(code)

native.bar_chart(dict(zip(categorias, valores)))

code = '''
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

categorias = ['A', 'B', 'C', 'D']
valores = [25, 40, 30, 35]

plt.bar(categorias, valores)
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')

st.pyplot(plt)
'''

matplot.code(code)

# matplotlib
plt.bar(categorias, valores)
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')

matplot.pyplot(plt)

# plotly

code = '''
import streamlit as st
import plotly.graph_objs as go

categorias = ['A', 'B', 'C', 'D']
valores = [25, 40, 30, 35]

data = [
    go.Bar(
        x=categorias,
        y=valores,
    )
]

layout = go.Layout(
    title='Gráfico de Barras - Plotly',
    xaxis=dict(title='Categorias'),
    yaxis=dict(title='Valores')
)

fig = go.Figure(data=data, layout=layout)

st.plotly_chart(fig)
'''

plotly.code(code)

data = [
    go.Bar(
        x=categorias,
        y=valores,
    )
]

layout = go.Layout(
    title='Gráfico de Barras - Plotly',
    xaxis=dict(title='Categorias'),
    yaxis=dict(title='Valores')
)

fig = go.Figure(data=data, layout=layout)

plotly.plotly_chart(fig)