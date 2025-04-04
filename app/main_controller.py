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
        f"Create a 4-week training program focused on increasing strength in the exercises "
        f"The athlete's current PRs are:\n{pr_text}\n\n"
        f"You must provide him the exact weght in kg, like instead of give him this info '3 sets of 4 reps at 80%' say '3 sets of 4 reps at 80% in your case 120kg'  "
        f"The program should include weekly frequency, load progression, "
        f"volume, and intensity. Present the plan week by week in a clear and organized manner. "
        f"Write and return the response using only <h3> and <p> HTML tags."
    )


    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        treino = response.text

        return jsonify({'planoTreino': treino})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
