from flask import Flask, request, jsonify
from user_service import UserService

app = Flask(__name__)
user_service = UserService()

@app.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    result, code = user_service.create_user(data)
    return jsonify(result), code

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result, code = user_service.delete_user(user_id)
    return jsonify(result), code

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify(user), 200
    else:
        return "User not found", 404

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    data = request.json
    result, code = user_service.update_user(user_id, data)
    return jsonify(result), code


if __name__ == '__main__':
    app.run(debug=True)
