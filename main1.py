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

if __name__ == '__main__':
    app.run(debug=True)
