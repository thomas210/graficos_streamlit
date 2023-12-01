import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.title("Radar")

st.write("Mostra valores múltiplos em diferentes eixos partindo de um ponto central.")

st.write("Exemplos")
st.write("Resultado geral de modelos em diferentes métricas")
st.write("Um gráfico de radar que compara as habilidades de um jogador em diferentes aspectos do jogo, como velocidade, precisão, resistência, etc.")
st.write("Sim, exatamente como em FIFA ou Bomba patch (100% atualizado), entre outros")
st.write("Etc...")

native, matplot, plotly = st.tabs(["Native Streamlit", "Matplotlib", "Plotly"])

# dados
categorias = ['A', 'B', 'C', 'D']
valores = [4, 3, 2, 5]

# native
native.error('Opa, não temos gráfico desse tipo')

# matplotlib
code = '''
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

categorias = ['A', 'B', 'C', 'D']
valores = [4, 3, 2, 5]

plt.figure(figsize=(6, 6))
plt.subplot(polar=True)
plt.plot(categorias + [categorias[0]], valores + [valores[0]], marker='o')
plt.fill(categorias, valores, 'blue', alpha=0.3)
plt.title('Gráfico de Radar')

st.pyplot(plt)
'''

matplot.code(code)

plt.figure(figsize=(6, 6))
plt.subplot(polar=True)
plt.plot(categorias + [categorias[0]], valores + [valores[0]], marker='o')
plt.fill(categorias, valores, 'blue', alpha=0.3)
plt.title('Gráfico de Radar')

matplot.pyplot(plt)

# plotly

code = '''
import streamlit as st
import plotly.graph_objects as go

categorias = ['A', 'B', 'C', 'D']
valores = [4, 3, 2, 5]

fig = go.Figure(data=go.Scatterpolar(r=valores, theta=categorias, fill='toself'))
fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
    title='Gráfico de Radar - Plotly no Streamlit'
)

st.plotly_chart(fig)
'''

plotly.code(code)

fig = go.Figure(data=go.Scatterpolar(r=valores, theta=categorias, fill='toself'))
fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
    title='Gráfico de Radar - Plotly no Streamlit'
)

plotly.plotly_chart(fig)