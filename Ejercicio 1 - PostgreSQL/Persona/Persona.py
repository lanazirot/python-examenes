import sys        
sys.path.append('C:/Examen - Postgresql')
from logger_base import log

class Persona:
    def __init__(self, idpersona=None, nombre=None, edad=None, correo=None) -> None:
        self._idpersona = idpersona
        self._nombre = nombre
        self._edad = edad
        self._correo = correo

    @property
    def idpersona(self):
        return self._idpersona

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def correo(self):
        return self._correo
    
    def __str__(self) -> str:
        return f"\nId Persona: {self._idpersona} \nNombre: {self._nombre} \nEdad: {self._edad} \nCorreo: {self._correo} \n"