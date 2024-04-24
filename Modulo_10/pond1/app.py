from flask import Flask, jsonify, request, make_response
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
auth = HTTPBasicAuth()

SWAGGER_URL = '/docs'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Simple CRUD Application"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

users = {
    "paulo": generate_password_hash("senha1"),
    "user2": generate_password_hash("senha2")
}

tasks = []

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.route('/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
@auth.login_required
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return make_response(jsonify({"message": "O título da tarefa é obrigatório"}), 400)
    task_id = len(tasks) + 1
    data['id'] = task_id
    tasks.append(data)
    return make_response(jsonify(data), 201)

@app.route('/tasks/<int:task_id>', methods=['GET'])
@auth.login_required
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task)
    else:
        return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
@auth.login_required
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        data = request.get_json()
        task.update(data)
        return jsonify(task)
    else:
        return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
@auth.login_required
def delete_task(task_id):
    global tasks
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        tasks = [task for task in tasks if task['id'] != task_id]
        return make_response(jsonify({"message": "Tarefa deletada"}), 200)
    else:
        return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)

if __name__ == '__main__':
    app.run(debug=True, threaded=False)
