from flask import Flask, jsonify, request
from http import HTTPStatus
from src.controller import UserController as controller

app = Flask(__name__)

controller = controller()

@app.get("/users")
def get_users():
    return jsonify(controller.get_users()), HTTPStatus.OK

@app.get("/users/<int:user_id>")
def get_user(user_id):
    try:
        return jsonify(controller.get_user(user_id)), HTTPStatus.OK
    except KeyError:
        return jsonify({"message": "User not found"}), HTTPStatus.NOT_FOUND
    
@app.post("/users")
def add_user():
    user_info = request.json
    controller.add_user(user_info)
    return jsonify({"message": "User added"}), HTTPStatus.CREATED
    
if __name__ == "__main__": 
    app.run(debug=True)