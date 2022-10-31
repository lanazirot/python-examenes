import string
from app import db
from dataclasses import dataclass

@dataclass
class Escuela(db.Model):
    
    id: int
    nombre: str
    direccion: str
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(255))
    
@dataclass
class Maestro(db.Model):
    
    id: int
    nombre: str
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    pass

class Alumno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    pass

class Materia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50))
    pass

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50))
    pass