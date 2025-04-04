from flask import Blueprint, request, jsonify
import google.generativeai as genai
from app.senha import GEMINI_API_KEY

main_controller = Blueprint('main_controller', __name__)

# Configura a API do Gemini
genai.configure(api_key=GEMINI_API_KEY)

@main_controller.route('/treino', methods=['POST'])
def gerar_treino():
    data = request.get_json()

    nome = data.get('name')
    peso_corporal = data.get('bodyWeight')
    prs = data.get('prs', [])

    if not nome or not peso_corporal or not prs:
        return jsonify({'error': 'Dados incompletos: name, bodyWeight e prs são obrigatórios'}), 400

    pr_text = "\n".join([f"{pr['exercise']}: {pr['weight']} kg" for pr in prs])

    prompt = (
        f"Crie um plano de treino de 4 semanas focado em aumentar a força nos três grandes levantamentos "
        f"(squat, bench press e deadlift) para o atleta {nome}, que pesa {peso_corporal} kg.\n\n"
        f"Os PRs atuais dele são:\n{pr_text}\n\n"
        f"O plano deve incluir frequência semanal, progressão de carga, variações de exercício, "
        f"volume e intensidade. Apresente o plano semana a semana de forma organizada."
    )

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        treino = response.text

        return jsonify({'planoTreino': treino})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
