from flask import Flask, jsonify, request
from http import HTTPStatus
from src.controller import UserController as controller

app = Flask(__name__)

controller = controller()

@app.get("/users")
def get_users():
    return controller.get_users()
@app.get("/users/<int:user_id>")
def get_user(user_id):
    return controller.get_user(user_id)
   
@app.post("/users")
def add_user():
    return controller.add_user(request.json)
@app.patch("/users/<int:user_id>")
def patch_user(user_id):
    return controller.patch_user(user_id, request.json)
@app.delete("/users/<int:user_id>")
def delete_user(user_id):
    return controller.delete_user(user_id)
if __name__ == "__main__": 
    app.run(debug=True)