from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    name = db.Column(db.String(100), nullable=False)


    def serialize(self): return {'id':self.id, 'name':self.name, 'login':self.login}
