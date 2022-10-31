import sys        
sys.path.append('C:/Examen - Postgresql')
from logger_base import log
class Contrato:
    def __init__(self, idcontrato=None, numcontrato=None, costo=None, fechainicio=None, fechafin=None) -> None:
        self._idcontrato = idcontrato
        self._numcontrato = numcontrato
        self._costo = costo
        self._fechainicio = fechainicio
        self._fechafin = fechafin

    @property
    def idcontrato(self):
        return self._idcontrato

    @property
    def numcontrato(self):
        return self._numcontrato

    @property
    def costo(self):
        return self._costo

    @property
    def fechainicio(self):
        return self._fechainicio

    @property
    def fechafin(self):
        return self._fechafin
    
    def __str__(self) -> str:
        return f"\nId Contrato: {self._idcontrato} \nNum. Contrato: {self._numcontrato} \nCosto: ${self._costo} \nFecha de inicio: {self._fechainicio} \nFecha final: {self._fechafin} \n"