from flask import Flask, jsonify
import os 

app = Flask(__name__)

jogos = [
    {"nome": "Cookie Run Kingdom", "genero": "RPG"},
    {"nome": "Brawl Stars", "genero": "MOBA"},
    {"nome": "HayDay", "genero": "RPG"},
    {"nome": "Roblox", "genero": "Sandbox"},
    {"nome": "Clash of Clans", "genero": "Estratégia"}
]

@app.route("/jogos", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Jogos - Acesse /jogos"})

@app.route("/", methods=["GET"])
def listar_jogos():
    return jsonify(jogos)

if __name__ == "_main_":
   port = int(os.environ.get("PORT,",5000))
   app.run(host="0.0.0.0", port=port)