import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

st.title("Histograma")

st.write("Mostra a distribuição de frequência de dados contínuos. Visualizar a distribuição normal dos elementos")

st.write("Exemplos")
st.write("Distribuição das alturas de alunos em uma sala de aula")
st.write("Distribuição de idades dos participantes de um concurso")
st.write("Etc...")

native, matplot, plotly = st.tabs(["Native Streamlit", "Matplotlib", "Plotly"])

# dados
dados = np.random.normal(0, 1, 1000)

# native
native.error('Opa, não temos gráfico desse tipo')

# matplotlib
code = '''
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

dados = np.random.normal(0, 1, 1000)

plt.hist(dados, bins=30)
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma')

st.pyplot(plt)
'''

matplot.code(code)

plt.hist(dados, bins=30)
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma')

matplot.pyplot(plt)

# plotly

code = '''
import streamlit as st
import plotly.express as px
import numpy as np

dados = np.random.normal(0, 1, 1000)

fig = px.histogram(x=dados, nbins=30, title='Histograma - Plotly no Streamlit')

# Exibindo o gráfico no Streamlit
st.plotly_chart(fig)
'''

plotly.code(code)

fig = px.histogram(x=dados, nbins=30, title='Histograma - Plotly no Streamlit')

plotly.plotly_chart(fig)