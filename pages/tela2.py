import streamlit as st


st.slider('Qtd de dias internado', min_value=0, max_value=720)


with st.form(key="calculadora"):
    numero1 = st.number_input("Digite o primeiro numero", min_value=0)

    numero2 = st.number_input("Digite o segundo numero numero", min_value=0)

    operacao = st.selectbox("Escolha operação", ["Soma", "Subtração", "Divisão", "Multiplicação"])

    if (st.form_submit_button("Realizar calculo")):
        if (operacao == "Soma"):
            resultado = numero1 + numero2
        elif (operacao == "Subtração"):
            resultado = numero1 - numero2
        elif (operacao == "Divisão"):
            resultado = numero1 / numero2
        elif (operacao == "Multiplicação"):
            resultado = numero1 * numero2
    
        st.write(resultado)
