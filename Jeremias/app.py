from flask import Flask, render_template, request, jsonify
from chatbot import responder

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/perguntar", methods=["POST"])
def perguntar():
    try:
        dados = request.get_json()
        if not dados or "pergunta" not in dados:
            return jsonify({"resposta": "Erro: pergunta não recebida."}), 400

        pergunta = dados["pergunta"]
        resposta = responder(pergunta)
        return jsonify({"resposta": resposta})

    except Exception as e:
        print(f"Erro ao processar pergunta: {e}")
        return jsonify({"resposta": "Erro interno no servidor."}), 500

if __name__ == "__main__":
    app.run(debug=True)

    