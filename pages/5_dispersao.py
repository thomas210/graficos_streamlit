import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import plotly.express as px

st.title("Dispersão")

st.write("Mostra a relação entre duas ou mais variáveis")

st.write("Exemplos")
st.write("Um diagrama de dispersão que representa a relação entre o tempo de estudo e a pontuação em um exame")
st.write("Relação entre renda, nota e realização de atividades dos alunos")
st.write("Etc...")

native, matplot, plotly = st.tabs(["Native Streamlit", "Matplotlib", "Plotly"])

# dados
x = np.random.rand(100)
y = np.random.rand(100)

# native
native.error('Opa, não temos gráfico desse tipo')

# matplotlib
code = '''
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Diagrama de Dispersão')

st.pyplot(plt)
'''

matplot.code(code)

plt.scatter(x, y)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Diagrama de Dispersão')

matplot.pyplot(plt)

# plotly

code = '''
import streamlit as st
import plotly.express as px

x = np.random.rand(100)
y = np.random.rand(100)

fig = px.scatter(x=x, y=y, title='Gráfico de Dispersão - Plotly no Streamlit')

st.plotly_chart(fig)
'''

plotly.code(code)

fig = px.scatter(x=x, y=y, title='Gráfico de Dispersão - Plotly no Streamlit')

plotly.plotly_chart(fig)