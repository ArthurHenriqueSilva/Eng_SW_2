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
