import sys        
sys.path.append('C:/Examen - Postgresql')
from logger_base import log
class Contrato_persona:
    def __init__(self, id=None, idpersona=None, idcontrato=None) -> None:
        self._id = id
        self._idpersona = idpersona
        self._idcontrato = idcontrato

    @property
    def id(self):
        return self._id
    @property
    def idpersona(self):
        return self._idpersona

    @property
    def idcontrato(self):
        return self._idcontrato
    
    def __str__(self) -> str:
        return f"\nId: {self._id} \nId Persona: {self._idpersona} \nId Contrato: {self._idcontrato} \n"