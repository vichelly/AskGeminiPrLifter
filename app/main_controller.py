from flask import Blueprint, request, jsonify
import google.generativeai as genai
from app.senha import GEMINI_API_KEY

main_controller = Blueprint('main_controller', __name__)

# Configura a API do Gemini
genai.configure(api_key=GEMINI_API_KEY)

@main_controller.route('/treino', methods=['POST'])
def gerar_treino():
    prs = request.get_json()

    if not isinstance(prs, list) or not prs:
        return jsonify({'error': 'Formato inválido: esperado uma lista de PRs'}), 400

    # Monta o texto com os PRs
    pr_text = "\n".join([f"{pr['exercise'].capitalize()}: {pr['kg']} kg" for pr in prs])

    # Prompt para o Gemini
    prompt = (
        f"Crie um plano de treino de 4 semanas focado em aumentar a força nos três grandes levantamentos "
        f"(squat, bench press e deadlift).\n\n"
        f"Os PRs atuais do atleta são:\n{pr_text}\n\n"
        f"O plano deve incluir frequência semanal, progressão de carga, variações de exercício, "
        f"volume e intensidade. Apresente o plano semana a semana de forma organizada e clara."
    )

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        treino = response.text

        return jsonify({'planoTreino': treino})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
