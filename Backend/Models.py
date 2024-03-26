from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import generate_password_hash, check_password_hash
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(15), nullable=False)


    def serialize(self): return {'id':self.id, 'name':self.name, 'email':self.email}
    
    def set_password(self, password): self.password = generate_password_hash(password)

    def check_password(self, password): return check_password_hash(self.password, password)

class FolhaPagamento(db.Model):
    __tablename__ = 'folha_pagamento'

    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    mes = db.Column(db.Integer, nullable=False)    
    ano = db.Column(db.Integer, nullable=False)    
    nome = db.Column(db.String(100), nullable=False)
    lotacao = db.Column(db.String(100))
    cargo = db.Column(db.String(100))
    remuneracao = db.Column(db.Double)
    vantagens = db.Column(db.Double)
    subsidio_comissao = db.Column(db.Double)
    indenizacoes = db.Column(db.Double)
    vantagens_eventuais = db.Column(db.Double)
    gratificacoes = db.Column(db.Double)
    total_credito = db.Column(db.Double)
    previdencia_publica = db.Column(db.Double)
    imposto_renda = db.Column(db.Double)
    descontos = db.Column(db.Double)
    retencao_teto = db.Column(db.Double)
    total_debitos = db.Column(db.Double)
    rendimento_liquido = db.Column(db.Double)
    remuneracao_orgao_origem = db.Column(db.Double)
    diarias = db.Column(db.Double)

    def serialize(self): return {'id':self.id, 'mes':self.mes, 'ano':self.ano, 'nome':self.nome,
                                 'lotacao':self.lotacao, 'cargo':self.cargo,
                                 'remuneracao':self.remuneracao, 'vantagens':self.vantagens,
                                 'subsidio_comissao':self.subsidio_comissao, 'indenizacoes':self.indenizacoes,
                                 'vantagens_eventuais':self.vantagens_eventuais, 'gratificacoes':self.gratificacoes,
                                 'total_credito':self.total_credito, 'previdencia_publica':self.previdencia_publica,
                                 'imposto_renda':self.imposto_renda, 'descontos':self.descontos,
                                 'retencao_teto':self.retencao_teto, 'total_debitos':self.total_debitos,
                                 'rendimento_liquido':self.rendimento_liquido,
                                 'remuneracao_orgao_origem':self.remuneracao_orgao_origem,
                                 'diarias':self.diarias}

class Favorito(db.Model):
    __tablename__ = 'favorito'
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id_owner = db.Column(db.Integer, db.ForeignKey('users.id'))
    mes = db.Column(db.Integer)
    ano = db.Column(db.Integer)
    tipo_servidor = db.Column(db.String(100))
    cargo = db.Column(db.String(100))
    nome_servidor = db.Column(db.String(200))
    limite_superior_remun = db.Column(db.Double)
    limite_inferior_remun = db.Column(db.Double)
    def serialize(self): return {'id': self.id, 'id_owner': self.id_owner, 'mes': self.mes,
                                  'ano': self.ano, 'tipo_servidor': self.tipo_servidor,
                                  'cargo': self.cargo, 'nome_servidor': self.nome_servidor, 
                                  'limite_superior_remun': self.limite_superior_remun,
                                  'limite_inferior_remun': self.limite_inferior_remun
                                  }