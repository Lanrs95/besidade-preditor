# 🧠 Preditor de Obesidade com Machine Learning

Este projeto foi desenvolvido como parte do desafio técnico da pós-graduação em Data Analytics (POSTECH). O objetivo foi construir um modelo preditivo capaz de classificar o nível de obesidade de uma pessoa com base em características pessoais, hábitos alimentares e estilo de vida.

---

## 🔗 Acesse o aplicativo online

👉 [Clique aqui para testar o modelo em tempo real](https://besidade-preditor-xxkq5zu2q5ftvzbmhnzyhp.streamlit.app/)

---

## 📊 Objetivo

Desenvolver um modelo de Machine Learning capaz de prever o nível de obesidade de um indivíduo com base em dados coletados via formulário, incluindo:

- Idade, altura, peso
- Alimentação e prática de atividades físicas
- Hábito de fumar, histórico familiar e outros

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas, NumPy, Scikit-learn
- Matplotlib, Seaborn
- Streamlit
- Git e GitHub

---

## 📁 Estrutura do Projeto

```
📦 besidade-preditor/
├── app.py                    # Aplicação web em Streamlit
├── modelo_obesidade.pkl      # Pipeline de ML treinado (pré-processamento + modelo)
├── Obesity.csv               # Dataset original
├── obesity-analise.ipynb     # Notebook com EDA e modelagem
├── requirements.txt          # Bibliotecas necessárias
└── README.md
```

---

## 🔍 Análise Exploratória (EDA)

- Nenhum valor nulo identificado
- Variáveis auxiliares criadas: `IMC`, `Risco Alimentar`, entre outras
- Gráficos mostraram forte correlação entre hábitos e obesidade
- Análises com `matplotlib`, `seaborn` e `pandas`

---

## 🤖 Modelos Testados

| Modelo                 | Acurácia (%) |
|-----------------------|--------------|
| ✅ Random Forest       | **93,14**     |
| Gradient Boosting     | 94,56         |
| Logistic Regression   | 86,99         |
| K-Nearest Neighbors   | 82,03         |

O modelo escolhido para deploy foi o **Random Forest**, por apresentar:

- Alta acurácia e robustez
- F1-score elevado em todas as classes
- Boa generalização validada com cross-validation

---

## 🔄 Validação Cruzada

Para garantir a generalização do modelo, foi aplicada validação cruzada com 5 folds:

- **Acurácia média:** 92,38%
- **Desvio padrão:** 11,21%
- Resultados consistentes em diferentes subconjuntos de dados

---

## ▶️ Como rodar o projeto localmente

```bash
git clone https://github.com/Lanrs95/besidade-preditor.git
cd besidade-preditor
pip install -r requirements.txt
streamlit run app.py
```

---

## 👤 Autor

**Allan Ribeiro da Silva**  
Desenvolvido como parte da Pós-Graduação em Data Analytics – POSTECH  
📫 [linkedin.com/in/allanrs](https://www.linkedin.com/in/allanrs)
