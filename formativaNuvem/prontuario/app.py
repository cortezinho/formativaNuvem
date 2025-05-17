from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

prontuarios = {}

@app.route('/prontuarios', methods=['POST'])
def criar_prontuario():
    data = request.get_json()
    consulta_id = data.get('consulta_id')
    consultas = requests.get('http://consulta:5000/consultas').json()
    if not any(str(i) == str(consulta_id) for i, _ in enumerate(consultas, start=1)):
        return jsonify({"erro": "Consulta inválida"}), 400
    prontuario_id = str(len(prontuarios) + 1)
    prontuarios[prontuario_id] = data
    return jsonify({"id": prontuario_id, **data}), 201

@app.route('/prontuarios/<id>', methods=['GET'])
def obter_prontuario(id):
    prontuario = prontuarios.get(id)
    if prontuario:
        return jsonify({"id": id, **prontuario})
    return jsonify({"erro": "Prontuário não encontrado"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)