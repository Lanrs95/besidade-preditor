# 🧠 Preditor de Obesidade com Machine Learning

Este projeto foi desenvolvido como parte do desafio técnico da pós-graduação em Data Analytics. A proposta foi construir um modelo preditivo capaz de classificar o nível de obesidade de uma pessoa com base em características pessoais, hábitos alimentares e estilo de vida.

---

## 🔗 Acesse o aplicativo online

👉 [Clique aqui para testar o modelo em tempo real](https://besidade-preditor-2us4wnkvaologr3wgyv972.streamlit.app/)

---

## 📊 Objetivo

Desenvolver um modelo de Machine Learning capaz de prever o nível de obesidade de um indivíduo a partir de um conjunto de variáveis brutas fornecidas por um formulário.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Pandas, NumPy, Scikit-learn**
- **Matplotlib, Seaborn**
- **Streamlit**
- **Git/GitHub**

---

## 📁 Estrutura do Projeto


---

## 🔍 Análise Exploratória

- Nenhum valor nulo encontrado no dataset
- Criadas variáveis auxiliares como IMC e Risco Alimentar para estudo
- Gráficos mostraram forte relação entre estilo de vida e obesidade
- Todas as análises foram feitas com `matplotlib`, `seaborn` e `pandas`

---

## 🤖 Modelos Testados

| Modelo                | Acurácia (%) |
|----------------------|--------------|
| Random Forest         | **93,14%**   |
| Gradient Boosting     | 94,56%       |
| Logistic Regression   | 86,99%       |
| K-Nearest Neighbors   | 82,03%       |

✅ O modelo escolhido para deploy foi o **Random Forest**, por apresentar:
- Alta acurácia
- Robustez na matriz de confusão
- Ótima performance por classe (f1-score elevado)

---

## 🔄 Validação Cruzada

Para garantir a generalização do modelo, foi aplicada validação cruzada (`cv=5`):

- **Acurácia média:** 92,38%
- **Desvio padrão:** 11,21%
- Isso mostra consistência do modelo mesmo em diferentes divisões dos dados.

---

## 🧪 Como rodar o projeto localmente

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositori
pip install -r requirements.txt
streamlit run app.py


## Autor: Allan Ribeiro da Silva
