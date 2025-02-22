from datetime import datetime

class UserRepository:
    def __init__(self) -> None:
        self.users = {}
        self.user_id = 0

    def add_user(self, user_info:dict) -> None:
        user = {
            "id": self.user_id,
            "name": user_info["firstName"],
            "last_name": user_info["lastName"],
            "age": datetime.year - user_info["birthYear"],
            "group": user_info["group"]
        }
        self.users[self.user_id] = user
        self.user_id += 1
    def get_users(self) -> dict:
        return self.users

    def get_user(self, user_id:int) -> dict:
        return self.users[user_id]