from http import HTTPStatus

class UserController:
    def __init__(self, repository) -> None:
        self.repository = repository

    def add_user(self, user_info: dict) -> tuple:
        try:
            self.repository.add_user(user_info)
            return {"message": "User added"}, HTTPStatus.CREATED
        except ValueError:
            return {"message": "Group does not exist"}, HTTPStatus.BAD_REQUEST

    def get_users(self) -> tuple:
        return self.repository.get_users(), HTTPStatus.OK

    def get_user(self, user_id: int) -> tuple:
        try:
            return self.repository.get_user(user_id), HTTPStatus.OK
        except KeyError:
            return {"message": "User not found"}, HTTPStatus.NOT_FOUND

    def patch_user(self, user_id: int, user_modify: dict) -> tuple:
        try:
            self.repository.patch_user(user_id, user_modify)
            return {"message": "User info modified"}, HTTPStatus.OK
        except KeyError:
            return {"message": "User not found"}, HTTPStatus.NOT_FOUND
        except ValueError:
            return {"message": "Group does not exist"}, HTTPStatus.BAD_REQUEST

    def delete_user(self, user_id: int) -> tuple:
        try:
            self.repository.delete_user(user_id)
            return {"message": "User deleted"}, HTTPStatus.OK
        except KeyError:
            return {"message": "User not found"}, HTTPStatus.NOT_FOUND