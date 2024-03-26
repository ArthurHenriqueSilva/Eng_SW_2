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

from flask import request

@app.route('/folha', methods=['GET'])
def get_folha_route():
    mes = request.args.get('mes')
    ano = request.args.get('ano')
    nome = request.args.get('nome')
    lotacao = request.args.get('lotacao')
    cargo = request.args.get('cargo') 
    remuneracao = request.args.get('remuneracao') 
    vantagens = request.args.get('vantagens') 
    subsidio_comissao = request.args.get('subsidio_comissao') 
    indenizacoes = request.args.get('indenizacoes') 
    vantagens_eventuais = request.args.get('vantagens_eventuais') 
    gratificacoes = request.args.get('gratificacoes') 
    total_credito = request.args.get('total_credito') 
    previdencia_publica = request.args.get('previdencia_publica') 
    imposto_renda = request.args.get('imposto_renda') 
    descontos = request.args.get('descontos') 
    retencao_teto = request.args.get('retencao_teto') 
    total_debitos = request.args.get('total_debitos') 
    rendimento_liquido = request.args.get('rendimento_liquido') 
    remuneracao_orgao_origem = request.args.get('remuneracao_orgao_origem') 
    diarias = request.args.get('diarias')

    folha = Control.Folha_Pagamento_Controller.get_folha(mes, ano, nome, lotacao, cargo, remuneracao, vantagens, subsidio_comissao,
                                            indenizacoes, vantagens_eventuais, gratificacoes, total_credito, previdencia_publica,
                                            imposto_renda, descontos, retencao_teto, total_debitos, rendimento_liquido,
                                            remuneracao_orgao_origem, diarias)
    if folha:
        return jsonify({'folha': [f.serialize() for f in folha]})
    return jsonify(Responses.folha_not_found), 404

@app.route('/consulta', methods=['GET'])
def consultar_dados():

    mes = int(request.args.get('mes'))
    ano = int(request.args.get('ano'))
    lotacao = request.args.get('lotacao')
    cargo = request.args.get('cargo')
    nome = request.args.get('nome')
    lim_inferior_remun = float(request.args.get('lim_inferior_remun'))
    lim_superior_remun = float(request.args.get('lim_superior_remun'))
    id = request.args.get('id')

    consulta = Control.Consulta_Controller.get_busca(mes, ano, lotacao, cargo,
                                                    nome, lim_inferior_remun,
                                                    lim_superior_remun, id)

    if consulta:
        return jsonify(consulta)
    else:
        return jsonify({'message': 'Nenhum resultado encontrado'}), 404


@app.route('/favoritos/<int:id_owner>', methods=['GET'])
def get_favoritos_route(id_owner):
    favoritos = Control.Favorito_Controller.get_favoritos(id_owner)
    if not favoritos: return jsonify(Responses.favoritos_not_found), 404
    return jsonify(favoritos=[favorito.serialize() for favorito in favoritos])

@app.route('/favoritos', methods=['POST'])
def add_favorito_route():
    try:
        data = request.json
        id_owner = data.get('id_owner')
        mes = data.get('mes')
        ano = data.get('ano')
        tipo_servidor = data.get('tipo_servidor')
        cargo = data.get('cargo')
        nome_servidor = data.get('nome_servidor')
        limite_superior_remun = data.get('limite_superior_remun')
        limite_inferior_remun = data.get('limite_inferior_remun')
        Control.Favorito_Controller.create_favorito(id_owner=id_owner, mes=mes, ano=ano, tipo_servidor=tipo_servidor,
                                                              cargo=cargo, nome_servidor=nome_servidor,
                                                              limite_superior_remun=limite_superior_remun,
                                                              limite_inferior_remun=limite_inferior_remun)
        return jsonify(Responses.favorito_created)
    except Exception as e:
        md.db.session.rollback()
        return jsonify(error=str(e)), 500

@app.route('/favoritos', methods=['DELETE'])
def delete_favorito_route():
    try:
      id = request.json.get('id')
      if Control.Favorito_Controller.delete_favorito(id): return jsonify(Responses.favorito_deleted)
      return jsonify(Responses.favoritos_not_found), 404
    except Exception as e:
        md.db.session.rollback()
        return jsonify(error=str(e)), 500


if __name__ == '__main__':
    with app.app_context():
        md.db.create_all()
    app.run(debug=True)