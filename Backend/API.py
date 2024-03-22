from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import Models as md
import Controllers as Control
import Responses

app = Flask('app')
env = 'test'
# env = 'prod'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///production_database.db' if env == 'prod' else 'sqlite:///test_database.db'
md.db.init_app(app)

@app.route('/')
def hello_world_backend():
    return jsonify(Responses.hello_world)

@app.route('/users', methods=['POST'])
def create_user_route():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    if not name or not email or not password: return jsonify(Responses.credentials_required), 400
    try:
        user = Control.User_controller.create_user(name, email, password)
        return jsonify(user_created={'message': 'User created successfully'})
    except Exception as e:
        md.db.session.rollback()
        return jsonify(error=str(e)), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_route(user_id):
    user = Control.User_controller.get_user_by_id(user_id)
    if user: return jsonify({'user': user.serialize()})
    return jsonify(Responses.user_not_found), 404

@app.route('/users', methods=['GET'])
def get_all_users_route():
    users = Control.User_controller.query_all()
    if not users: return jsonify(Responses.user_not_found)
    return jsonify(users=[user.serialize() for user in users])

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.json
    new_name = data.get('name')
    new_email = data.get('email')
    new_password = data.get('password')
    try:
        user = Control.User_controller.update_user(user_id, new_name, new_email, new_password)
        if user: return jsonify(Responses.user_updated)
        return jsonify(Responses.user_not_found), 404
    except Exception as e:
        md.db.session.rollback()
        return jsonify(error=str(e)), 500

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    try:
        deleted = Control.User_controller.delete_user(user_id)
        if deleted: return jsonify(Responses.user_deleted)
        return jsonify(Responses.user_not_found), 404
    except Exception as e:
        md.db.session.rollback()
        return jsonify(error=str(e)), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password: return jsonify(Responses.credentials_required), 400

    try:
        user = Control.User_controller.login(email, password)
        if user is None: return jsonify(Responses.invalid_email), 401
        if user is False: return jsonify(Responses.invalid_password), 401
        return jsonify({'message': 'Login successful', 'user': user.serialize()})
    except Exception as e:
        md.db.session.rollback()
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    with app.app_context():
        md.db.create_all()
    app.run(debug=True)
