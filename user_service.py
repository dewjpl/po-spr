class UserService:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def get_all_users(self):
        return list(self.users.values())

    def get_user_by_id(self, user_id):
        return self.users.get(user_id)