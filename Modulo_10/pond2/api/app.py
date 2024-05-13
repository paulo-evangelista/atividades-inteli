from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

print("Starting API...")

app = Flask(__name__)
CORS(app)

tasks = []


@app.route('/getAllTasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/createTask', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return make_response(jsonify({"message": "O título da tarefa é obrigatório"}), 400)
    task_id = len(tasks) + 1
    data['id'] = task_id
    tasks.append(data)
    print("\ncreateTask: ", data)
    return make_response(jsonify(data), 201)

@app.route('/getTask/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task)
    else:
        return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)

@app.route('/updateTask/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        data = request.get_json()
        task.update(data)
        print("\nupdateTask: ", task)
        return jsonify(task)
    else:
        return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)

@app.route('/deleteTask/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        tasks = [task for task in tasks if task['id'] != task_id]
        print("\ndeleteTask: ", task)
        return make_response(jsonify({"message": "Tarefa deletada"}), 200)
    else:
        return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
