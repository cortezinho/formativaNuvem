from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

consultas = []

@app.route('/consultas', methods=['POST'])
def agendar_consulta():
    data = request.get_json()
    paciente_id = data.get('paciente_id')
    resp = requests.get(f'http://paciente:5000/pacientes/{paciente_id}')
    if resp.status_code != 200:
        return jsonify({"erro": "Paciente inválido"}), 400
    consultas.append(data)
    return jsonify(data), 201

@app.route('/consultas', methods=['GET'])
def listar_consultas():
    return jsonify(consultas)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)