import streamlit as st
import pandas as pd
import joblib

# Carregar o modelo treinado
modelo = joblib.load('modelo_obesidade.pkl')

st.title("Preditor de Obesidade")
st.markdown("Preencha as informações abaixo para prever o nível de obesidade.")

with st.form(key='formulario_obesidade'):
    st.markdown("### 👤 Dados Pessoais")
    genero = st.selectbox('Gênero', ['Masculino', 'Feminino'])
    idade = st.number_input('Idade', min_value=1, max_value=100, value=25)
    altura = st.number_input('Altura (em metros)', min_value=1.0, max_value=2.5, step=0.01, value=1.70)
    peso = st.number_input('Peso (em kg)', min_value=30.0, max_value=200.0, step=0.5, value=70.0)

    st.markdown("### 🧬 Histórico e Hábitos Alimentares")
    historico = st.radio('Tem histórico familiar de obesidade?', ['Sim', 'Não'])
    comida_calorica = st.radio('Consome comida calórica com frequência?', ['Sim', 'Não'])
    vegetais = st.slider('Frequência de vegetais na alimentação (0 a 3)', 0.0, 3.0, 2.0, step=0.5)
    refeicoes_dia = st.slider('Número de refeições principais por dia', 1.0, 4.0, 3.0, step=1.0)
    petiscos = st.selectbox('Frequência de petiscos entre refeições', ['Não', 'Às vezes', 'Frequentemente', 'Sempre'])
    controle_calorias = st.radio('Você controla as calorias consumidas?', ['Sim', 'Não'])

    st.markdown("### 🏃 Hábitos e Estilo de Vida")
    fumante = st.radio('Você fuma?', ['Sim', 'Não'])
    agua = st.slider('Quantidade de água por dia (0 a 3)', 0.0, 3.0, 2.0, step=0.5)
    atividade_fisica = st.slider('Frequência de atividade física (0 a 3)', 0.0, 3.0, 1.0, step=0.5)
    tempo_tecnologia = st.slider('Tempo em dispositivos por dia (0 a 3)', 0.0, 3.0, 2.0, step=0.5)
    alcool = st.selectbox('Frequência de consumo de álcool', ['Não', 'Às vezes', 'Frequentemente', 'Sempre'])
    transporte = st.selectbox('Meio de transporte mais utilizado', ['Carro', 'Moto', 'Bicicleta', 'Transporte Público', 'Caminhada'])

    submit_button = st.form_submit_button('Prever')

if submit_button:
    # Mapas de tradução para o modelo
    map_genero = {'Masculino': 'Male', 'Feminino': 'Female'}
    map_binario = {'Sim': 'yes', 'Não': 'no'}
    map_petiscos = {'Não': 'no', 'Às vezes': 'Sometimes', 'Frequentemente': 'Frequently', 'Sempre': 'Always'}
    map_transporte = {
        'Carro': 'Automobile',
        'Moto': 'Motorbike',
        'Bicicleta': 'Bike',
        'Transporte Público': 'Public_Transportation',
        'Caminhada': 'Walking'
    }

    entrada = pd.DataFrame([{
        'Genero': map_genero[genero],
        'Idade': idade,
        'Altura': altura,
        'Peso': peso,
        'Historico_Familiar': map_binario[historico],
        'Comida_Calorica_Frequente': map_binario[comida_calorica],
        'Vegetais_Frequentes': vegetais,
        'Refeicoes_Dia': refeicoes_dia,
        'Petiscos_Entre_Refeicoes': map_petiscos[petiscos],
        'Fumante': map_binario[fumante],
        'Agua_por_Dia': agua,
        'Controle_Calorias': map_binario[controle_calorias],
        'Atividade_Fisica': atividade_fisica,
        'Tempo_Tecnologia': tempo_tecnologia,
        'Consumo_Alcool': map_petiscos[alcool],
        'Transporte': map_transporte[transporte]
    }])

    # Predição
    predicao = modelo.predict(entrada)

    # Traduzir resposta
    map_resposta = {
        'Insufficient_Weight': 'Abaixo do peso',
        'Normal_Weight': 'Peso normal',
        'Overweight_Level_I': 'Sobrepeso nível I',
        'Overweight_Level_II': 'Sobrepeso nível II',
        'Obesity_Type_I': 'Obesidade tipo I',
        'Obesity_Type_II': 'Obesidade tipo II',
        'Obesity_Type_III': 'Obesidade tipo III'
    }
    resposta_pt = map_resposta.get(predicao[0], predicao[0])

    st.success(f'Nível de obesidade previsto: **{resposta_pt}**')