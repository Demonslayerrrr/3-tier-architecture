from datetime import date

class UserRepository:
    def __init__(self) -> None:
        self.users = {}
        self.user_id = 0

    def add_user(self, user_info:dict) -> None:
        user = {
            "id": self.user_id,
            "name": user_info["first_name"],
            "last_name": user_info["last_name"],
            "age": date.today().year - user_info["birth_year"],
            "group": user_info["group"]
        }
        self.users[self.user_id] = user
        self.user_id += 1
    def get_users(self) -> dict:
        return self.users

    def get_user(self, user_id:int) -> dict:
        return self.users[user_id]