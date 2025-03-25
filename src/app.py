from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def todos_list():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body",request_body)
    todos.append(request_body)  # Paso 2: Agregar el diccionario a la lista todos
    return jsonify(todos)  # Paso 3: Devolver la lista actualizada

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Asegurarse que la posición sea válida
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Índice fuera de rango"}), 404
    # Eliminar la tarea
    del todos[position]
    # Retornar la lista actualizada
    return jsonify(todos)






















# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)