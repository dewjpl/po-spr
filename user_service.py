class UserService:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def get_all_users(self):
        return list(self.users.values())

    def get_user(self, user_id):
        return self.users.get(user_id)

    def create_user(self, data):
        if not all(key in data for key in ("firstName", "lastName", "birthYear", "group")):
            return "Missing fields", 400
        user_id = self.next_id
        self.next_id += 1
        data['id'] = user_id
        self.users[user_id] = data
        return data, 200

    def update_user(self, user_id, data):
        user = self.users.get(user_id)
        if not user:
            return "User not found", 404
        user.update(data)
        return user, 200

    def delete_user(self, user_id):
        if user_id not in self.users:
            return "User not found", 404
        del self.users[user_id]
        return "User deleted successfully", 200
