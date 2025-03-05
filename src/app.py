from flask import Flask, request, jsonify
from src.controller import UserController as controller
from src.repository import UserRepository

app = Flask(__name__)

controller = controller(UserRepository())

@app.get("/users")
def get_users():
    json_data, status_code = controller.get_users()
    return jsonify(json_data), status_code
@app.get("/users/<int:user_id>")
def get_user(user_id):
    json_data, status_code =  controller.get_user(user_id)
    return jsonify(json_data), status_code
@app.post("/users")
def add_user():
    json_data,status_code = controller.add_user(request.json)
    return jsonify(json_data), status_code
@app.patch("/users/<int:user_id>")
def patch_user(user_id):
    json_data, status_code = controller.patch_user(user_id, request.json)
    return jsonify(json_data), status_code
@app.delete("/users/<int:user_id>")
def delete_user(user_id):
    json_data, status_code = controller.delete_user(user_id)
    return jsonify(json_data), status_code
if __name__ == "__main__": 
    app.run(debug=True)