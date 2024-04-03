from flask import Flask, request, jsonify

app = Flask(__name__)


eventos = [
    {"id": 1, "titulo": "Reunião", "data": "2024-04-05", "horario": "10:00"},
    {"id": 2, "titulo": "Almoço", "data": "2024-04-05", "horario": "12:00"}
]

@app.route('/eventos', methods=['GET'])
def listar_eventos():
    return jsonify(eventos)

@app.route('/eventos', methods=['POST'])
def criar_evento():
    dados = request.json
    novo_evento = {
        "id": len(eventos) + 1,
        "titulo": dados["titulo"],
        "data": dados["data"],
        "horario": dados["horario"]
    }
    eventos.append(novo_evento)
    return jsonify(novo_evento), 201


@app.route('/eventos/<int:evento_id>', methods=['GET'])
def visualizar_evento(evento_id):
    evento = [evento for evento in eventos if evento['id'] == evento_id]
    if len(evento) == 0:
        return jsonify({"erro": "Evento não encontrado"}), 404
    return jsonify(evento[0])


@app.route('/eventos/<int:evento_id>', methods=['PUT'])
def atualizar_evento(evento_id):
    dados = request.json
    evento = [evento for evento in eventos if evento['id'] == evento_id]
    if len(evento) == 0:
        return jsonify({"erro": "Evento não encontrado"}), 404
    evento[0]['titulo'] = dados['titulo']
    evento[0]['data'] = dados['data']
    evento[0]['horario'] = dados['horario']
    return jsonify(evento[0])


@app.route('/eventos/<int:evento_id>', methods=['DELETE'])
def excluir_evento(evento_id):
    evento = [evento for evento in eventos if evento['id'] == evento_id]
    if len(evento) == 0:
        return jsonify({"erro": "Evento não encontrado"}), 404
    eventos.remove(evento[0])
    return jsonify({"mensagem": "Evento excluído com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
