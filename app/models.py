from . import db
from sqlalchemy.orm import backref

class Estudante(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    Email = db.Column(db.String(20), nullable=False, unique=True)
    DataNascimento = db.Column(db.Integer(20), nullable=False)
    def __repr__(self):
        return f'<User {self.nome}>'

class Curso (db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    Duraçao = db.Column(db.String(20), nullable=False, unique=True)
    Preco = db.Column(db.Integer(20), nullable=False)

class Inscricoes (db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    IdEstudante = db.Column(db.Integer,db.ForieingKey(Estudante(Id)), nullable=False)
    IdCurso = db.Column(db.Integer,db.ForieingKey(Curso(Id)), nullable=False, unique=True)
    DataInscricao = db.Column(db.Integer(20), nullable=False)