from . import db
from sqlalchemy.orm import backref

class Estudante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    data_nascimento = db.Column(db.DateTime, nullable=False)
    def __repr__(self):
        return f'<User {self.nome}>'

class Curso (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nonlocalome = db.Column(db.String(120), nullable=False)
    duraçao = db.Column(db.String(20), nullable=False, unique=True)
    preco = db.Column(db.Integer(20), nullable=False)

class Inscricoes (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idEstudante = db.Column(db.Integer,db.ForeingKey('estudante.id'))
    idCurso = db.Column(db.Integer,db.ForeingKey('curso.id'))
    data_inscricao = db.Column(db.DateTime, nullable=False)