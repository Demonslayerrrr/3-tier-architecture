from src.repository import UserRepository
from http import HTTPStatus
from flask import jsonify, request

class UserController:
    def __init__(self) -> None:
        self.repository = UserRepository()
    
    def add_user(self, user_info:dict) -> None:
        try:
            user_info = request.json
            self.repository.add_user(user_info)
            return jsonify({"message": "User added"}), HTTPStatus.CREATED
        except ValueError:
            return jsonify({"message": "Group does not exist"}), HTTPStatus.BAD_REQUEST
    

    
    def get_users(self) -> dict:
        return jsonify(self.repository.get_users()), HTTPStatus.OK
    
    def get_user(self, user_id:int) -> dict:
        try:
            return jsonify(self.repository.get_user(user_id)), HTTPStatus.OK

        except KeyError:
            return jsonify({"message": "User not found"}), HTTPStatus.NOT_FOUND


    def patch_user(self, user_id:int, user_modify:dict) -> None:
        try:
            user_modify = request.json
            self.repository.patch_user(user_id,user_modify)
            return jsonify({"message": "User info modified"}),HTTPStatus.OK
        except KeyError:
            return jsonify({"message": "User not found"}), HTTPStatus.NOT_FOUND
        except ValueError:
            return jsonify({"message": "Group does not exist"}), HTTPStatus.BAD_REQUEST



    def delete_user(self, user_id: int) -> None:
        try:
            self.repository.delete_user(user_id)
            return jsonify({"message": "User deleted"}), HTTPStatus.OK
    
        except KeyError:
            return jsonify({"message": "User not found"}), HTTPStatus.NOT_FOUND
