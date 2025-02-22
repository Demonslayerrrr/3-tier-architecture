from src.repository import UserRepository

class UserController:
    def __init__(self) -> None:
        self.repository = UserRepository()
    
    def add_user(self, user_info:dict) -> None:
        self.repository.add_user(user_info)
    
    def get_users(self) -> dict:
        return self.repository.get_users()
    
    def get_user(self, user_id:int) -> dict:
        return self.repository.get_user(user_id)