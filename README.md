# 🏋️‍♂️ Powerlifting Training Generator API

Esta é uma API Flask que utiliza o **Google Gemini** para gerar um **plano de treino de 4 semanas** com base nos PRs (personal records) de um atleta de powerlifting.

---

## 🚀 Como funciona

Você envia uma lista com seus PRs para os exercícios principais (como squat, bench press, deadlift) e a API retorna um plano de treino baseado neles, com carga exata em kg, frequência semanal, progressão e volume.

---

## 📦 Requisitos

- Python 3.10+
- Flask
- google-generativeai
- python-dotenv
- Uma chave válida da API do Gemini

---


📥 Rota
POST /treino

Gera um plano de treino com base nos PRs fornecidos.
Corpo da requisição (JSON)
[
  { "exercise": "squat", "kg": 180 },
  { "exercise": "benchpress", "kg": 130 },
  { "exercise": "deadlift", "kg": 210 }
]
