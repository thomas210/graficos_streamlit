import streamlit as st

st.sidebar.write("aqui é o sidebar")

nome = st.text_input("Digite seu nome", help="esta e a janela de ajuda")

idade = st.number_input("Digite o numero", min_value=0)

if (st.button("clique aqui")):
    st.write(nome)

    st.write(idade)

# Group multiple widgets:
with st.form(key='my_form'):
  username = st.text_input('Username')
  password = st.text_input('Password')
  idade = st.number_input("Digite o numero", min_value=0)
  if (st.form_submit_button('Login')):
     st.write(username)
     st.write(password)
     st.write(idade)