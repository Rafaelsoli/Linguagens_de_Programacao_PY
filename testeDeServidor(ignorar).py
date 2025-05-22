from flask import Flask, request

app = Flask(__name__)

# Exemplo de variável global que seu slide pode ler
comando_recebido = None
-
@app.route("/comando", methods=["POST"])
def receber_comando():
    global comando_recebido
    comando = request.form.get("acao")
    print(f"Comando recebido: {comando}")
    comando_recebido = comando
    return "OK"

def obter_comando():
    global comando_recebido
    cmd = comando_recebido
    comando_recebido = None
    return cmd

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
