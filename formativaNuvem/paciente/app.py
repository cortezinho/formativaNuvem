from flask import Flask, request, jsonify
app = Flask(__name__)

pacientes = {}

@app.route('/pacientes', methods=['POST'])
def criar_paciente():
    data = request.get_json()
    paciente_id = str(len(pacientes) + 1)
    pacientes[paciente_id] = data
    return jsonify({"id": paciente_id, **data}), 201

@app.route('/pacientes/<id>', methods=['GET'])
def obter_paciente(id):
    paciente = pacientes.get(id)
    if paciente:
        return jsonify({"id": id, **paciente})
    return jsonify({"erro": "Paciente não encontrado"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
