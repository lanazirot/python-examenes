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

@dataclass
class Alumno(db.Model):
    
    id: int
    nombre: str
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    pass
@dataclass
class Materia(db.Model):
    
    id: int
    titulo: str
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50))
    pass

@dataclass
class Evento(db.Model):
    
    id: int
    descripcion: str
    
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50))
    pass