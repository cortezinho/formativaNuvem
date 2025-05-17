from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/plano_saude/cobertura/<procedimento>', methods=['GET'])
def verificar_cobertura(procedimento):
    coberto = procedimento.lower() in ["consulta", "exame", "cirurgia"]
    return jsonify({"coberto": coberto})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005)
