# Flask allows us to easily set up a server with @app.route()
from flask import Flask, request, jsonify

# This allows us to accept requests from our frontend
# which is on a different server.
from flask_cors import CORS

# Set up the app & tell it (with CORS) that we will allow 
# requests from our frontend, but no other place
app = Flask(__name__)
CORS(app, origins=['http://localhost:1234'])

# In-memory storage for tasks
# Each task: { 'id': int, 'description': str, 'completed': bool }
tasks = []
next_id = 1

# Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    global next_id
    data = request.json
    if not data or 'description' not in data:
        return jsonify({'error': 'Description is required'}), 400
    task = {
        'id': next_id,
        'description': data['description'],
        'completed': False
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201

# Delete a task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks.pop(i)
            return jsonify({'status': 'success'}), 200
    return jsonify({'error': 'Task not found'}), 404

# Mark a task as complete/incomplete
@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    data = request.json
    if not data or 'completed' not in data:
        return jsonify({'error': 'Completed status is required'}), 400
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = bool(data['completed'])
            return jsonify(task), 200
    return jsonify({'error': 'Task not found'}), 404

# (Optional) List all tasks for debugging
@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(tasks)

# This function will be triggered when the server receives a
# POST request at the URL '/hello'
@app.route('/hello', methods=['POST'])
def hello():
  # Grab the name the frontend sends us, which is in the 
  # { 'name': 'your name' } JSON object we are sent in the
  # request
  json = request.json
  name = json['name']

  # Send back a JSON object that has a message object for the
  # frontend to then display.
  return jsonify({ 'message': f'Hello {name}' })