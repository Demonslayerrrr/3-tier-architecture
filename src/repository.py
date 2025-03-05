from datetime import date

class UserRepository:
    def __init__(self) -> None:
        self.users = {}
        self.user_id = 0
        self.groups = ["user","premium", "admin"]
    def add_user(self, user_info:dict) -> None:
        if user_info["group"].lower() not in self.groups:
            raise ValueError()
        user = {
            "first_name": user_info["first_name"],
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

    def patch_user(self,user_id:int, user_modify:int) -> None:
        if user_id not in self.users.keys():
            raise KeyError()
        
        elif user_modify["group"].lower() not in self.groups:
            raise ValueError()

        user = {
            "first_name": user_modify["first_name"],
            "last_name": user_modify["last_name"],
            "age": date.today().year - user_modify["birth_year"],
            "group": user_modify["group"]
        }

        self.users[user_id] = user
        
    def delete_user(self, user_id:int) -> None:
        del self.users[user_id]