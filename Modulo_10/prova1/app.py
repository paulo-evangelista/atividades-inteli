from flask import Flask, jsonify, request, make_response

print("Starting API...")

app = Flask(__name__)

pedidos = []


@app.route('/novo', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'user' not in data or 'email' not in data or 'description' not in data:
        return make_response(jsonify({"message": "Preencha todos os campos (user, email e description)"}), 400)
    pedido_id = len(pedidos) + 1
    data['id'] = pedido_id
    pedidos.append(data)
    print("\ncreateTask: ", data)
    return make_response(jsonify({"id": data["id"]}), 201)

@app.route('/pedidos', methods=['GET'])
def get_tasks():
    return jsonify(pedidos)

@app.route('/pedidos/<int:pedido_id>', methods=['GET'])
def get_task(pedido_id):
    task = next((task for task in pedidos if task['id'] == pedido_id), None)
    if task:
        return jsonify(task)
    else:
        return make_response(jsonify({"message": "Pedido não encontrado"}), 404)

@app.route('/pedidos/<int:pedido_id>', methods=['PUT'])
def update_task(pedido_id):
    task = next((task for task in pedidos if task['id'] == pedido_id), None)
    if task:
        data = request.get_json()
        task.update(data)
        return make_response(jsonify({"message": "Tarefa atualizada"}), 200)
    else:
        return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)

@app.route('/pedidos/<int:pedido_id>', methods=['DELETE'])
def delete_task(pedido_id):
    global pedidos
    task = next((task for task in pedidos if task['id'] == pedido_id), None)
    if task:
        pedidos = [task for task in pedidos if task['id'] != pedido_id]
        print("\ndeleteTask: ", task)
        return make_response(jsonify({"message": "Tarefa deletada"}), 200)
    else:
        return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
