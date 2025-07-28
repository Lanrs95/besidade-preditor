import streamlit as st
import pandas as pd
import joblib

# Carregar o modelo treinado (pipeline completo)
modelo = joblib.load('modelo_obesidade.pkl')

st.title("Preditor de Obesidade")
st.markdown("Preencha as informações abaixo para prever o nível de obesidade.")

with st.form(key='formulario_obesidade'):
    st.markdown("### 👤 Dados Pessoais")
    genero = st.selectbox('Gênero', ['Male', 'Female'])
    idade = st.number_input('Idade', min_value=1, max_value=100, value=25)
    altura = st.number_input('Altura (em metros)', min_value=1.0, max_value=2.5, step=0.01, value=1.70)
    peso = st.number_input('Peso (em kg)', min_value=30.0, max_value=200.0, step=0.5, value=70.0)

    st.markdown("### 🧬 Histórico e Hábitos Alimentares")
    historico = st.radio('Tem histórico familiar de obesidade?', ['yes', 'no'])
    comida_calorica = st.radio('Consome comida calórica com frequência?', ['yes', 'no'])
    vegetais = st.slider('Frequência de vegetais na alimentação (0 a 3)', 0.0, 3.0, 2.0, step=0.5)
    refeicoes_dia = st.slider('Número de refeições principais por dia', 1.0, 4.0, 3.0, step=1.0)
    petiscos = st.selectbox('Frequência de petiscos entre refeições', ['no', 'Sometimes', 'Frequently', 'Always'])
    controle_calorias = st.radio('Você controla as calorias consumidas?', ['yes', 'no'])

    st.markdown("### 🏃 Hábitos e Estilo de Vida")
    fumante = st.radio('Você fuma?', ['yes', 'no'])
    agua = st.slider('Quantidade de água por dia (0 a 3)', 0.0, 3.0, 2.0, step=0.5)
    atividade_fisica = st.slider('Frequência de atividade física (0 a 3)', 0.0, 3.0, 1.0, step=0.5)
    tempo_tecnologia = st.slider('Tempo em dispositivos por dia (0 a 3)', 0.0, 3.0, 2.0, step=0.5)
    alcool = st.selectbox('Frequência de consumo de álcool', ['no', 'Sometimes', 'Frequently', 'Always'])
    transporte = st.selectbox('Meio de transporte mais utilizado', ['Automobile', 'Motorbike', 'Bike', 'Public_Transportation', 'Walking'])

    submit_button = st.form_submit_button('Prever')

if submit_button:
    # Montar DataFrame com as entradas do usuário
    entrada = pd.DataFrame([{
        'Genero': genero,
        'Idade': idade,
        'Altura': altura,
        'Peso': peso,
        'Historico_Familiar': historico,
        'Comida_Calorica_Frequente': comida_calorica,
        'Vegetais_Frequentes': vegetais,
        'Refeicoes_Dia': refeicoes_dia,
        'Petiscos_Entre_Refeicoes': petiscos,
        'Fumante': fumante,
        'Agua_por_Dia': agua,
        'Controle_Calorias': controle_calorias,
        'Atividade_Fisica': atividade_fisica,
        'Tempo_Tecnologia': tempo_tecnologia,
        'Consumo_Alcool': alcool,
        'Transporte': transporte
    }])

    # Fazer a previsão
    predicao = modelo.predict(entrada)

    st.success(f'Nível de obesidade previsto: **{predicao[0]}**')