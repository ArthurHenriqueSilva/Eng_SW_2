from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import Models as md
import Controllers as Control
import Responses


#Configurações de ambiente do app
app = Flask('app')
env = 'test'
#env = 'prod'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///production_database.db' if env == 'prod' else 'sqlite:///test_database.db'
md.db.init_app(app)


#Rotas da app
@app.route('/')
def hello_world_Backend():
    return jsonify(Responses.hello_world)

@app.route('/users', methods=['POST'])
def create_user_route():
    data = request.json
    user = Control.User.create_user(data['name'])
    return jsonify({'message':'User created succesfully', 'user':user.serialize()})


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_route(user_id):
    user = Control.User.get_user_by_id(user_id)
    if user:
        return jsonify({'user': user.serialize()})
    else:
        return jsonify(Responses.user_not_found_response), 404

@app.route('/users', methods=['GET'])
def get_all_users_route():
    users = Control.User.query.all()
    if not users:  return jsonify(Responses.user_not_found_response)
    return jsonify(users=[user.serialize() for user in users])
    

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.json
    user = Control.User.update_user(user_id, data['name'])
    if user: 
        return jsonify({'message': 'User updated successfully', 'user': user.serialize()})
    else: 
        return jsonify(Responses.user_not_found_response), 404
    
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    deleted_response = Control.User.delete_user(user_id)
    if deleted_response: 
        return jsonify(Responses.user_deleted_response)
    else: 
        return jsonify(Responses.user_not_found_response), 404
    
if __name__ == '__main__':
    with app.app_context():
        md.db.create_all()
    app.run(debug=True)
