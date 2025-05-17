from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

faturas = []

@app.route('/faturas', methods=['POST'])
def gerar_fatura():
    data = request.get_json()
    procedimento = data.get("procedimento")
    resp = requests.get(f'http://plano_saude:5000/plano_saude/cobertura/{procedimento}')
    if resp.status_code != 200 or not resp.json().get("coberto"):
        return jsonify({"erro": "Procedimento não coberto"}), 400
    faturas.append(data)
    return jsonify(data), 201

@app.route('/faturas', methods=['GET'])
def listar_faturas():
    return jsonify(faturas)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)