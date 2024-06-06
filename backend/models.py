from backend import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True , nullable=False)
    senha = db.Column(db.String, nullable=False)
    
    