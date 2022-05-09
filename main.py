from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from service.todo_service import TodoService

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

todo_service = TodoService()


@app.route("/todolist", methods=['GET', 'POST', 'PUT', 'DELETE'])
@cross_origin()
def todos_methods():
    if request.method == 'GET':
        filter = request.args.get("filter")
        if filter == "active":
            return jsonify(todo_service.get_todos(False))
        elif filter == "completed":
            return jsonify(todo_service.get_todos(True))
        else: # !!!
            return jsonify(todo_service.get_todos(None))

    elif request.method == 'POST':
        # if not isinstance(request.json["title"], str):
        #     raise "Server error, 403"
        title = request.json["title"]
        return jsonify(todo_service.add_todo(title))
    elif request.method == 'PUT':
        title = request.json["title"]
        completed = request.json["completed"]
        id = request.json["id"]
        return jsonify(todo_service.update_completed(id, title, completed))
    elif request.method == 'DELETE':
        id = request.json["id"]
        todo_service.delete(id)


@app.route("/delete/all")
def delete_all():
    if request.method == "DELETE":
        todo_service.delete_all()

if __name__ == "__main__":
    app.run(port=3000, host="0.0.0.0", debug=True)
