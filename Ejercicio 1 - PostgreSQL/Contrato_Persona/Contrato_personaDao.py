import sys        
sys.path.append('C:/Examen - Postgresql')
from Contrato_persona import Contrato_persona
from Conexion import Conexion
from CursorDelPool import CursorDelPool
from logger_base import log

class Contrato_personaDao:
    _SELECCIONAR = "SELECT * FROM contrato_persona ORDER BY id"
    _INSERTAR = "INSERT INTO contrato_persona(idpersona, idcontrato) Values(%s,%s)"
    _OBTENERCOSTOS = "SELECT SUM(c.costo) as suma FROM contrato_persona as cp INNER JOIN contrato as c ON c.idcontrato = cp.idcontrato INNER JOIN persona as p ON p.idpersona = cp.idpersona WHERE p.correo = %s"
    _OBTENERCONTRATO = "SELECT p.nombre, c.numcontrato, c.costo FROM contrato_persona as cp INNER JOIN contrato as c ON c.idcontrato = cp.idcontrato INNER JOIN persona as p ON p.idpersona = cp.idpersona WHERE p.correo = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                contrato_personas=[]
                for r in registros:
                    contrato_persona = Contrato_persona(r[0],r[1],r[2])
                    contrato_personas.append(contrato_persona)
                return contrato_personas

    @classmethod
    def insertar(cls,Contrato_persona):
        with CursorDelPool() as cursor:
            valores = (Contrato_persona.idpersona, Contrato_persona.idcontrato)
            cursor.execute(cls._INSERTAR,valores)
            log.debug("Se registro el id")
            return cursor.rowcount
    
    @classmethod
    def costostotal(cls,correo):
        with CursorDelPool() as cursor:
            valores = (correo,)
            cursor.execute(cls._OBTENERCOSTOS, valores)
            registros = cursor.fetchall()
            return registros
    
    @classmethod
    def obtenercontrato(cls,correo):
        with CursorDelPool() as cursor:
            valores = (correo,)
            cursor.execute(cls._OBTENERCONTRATO, valores)
            registros = cursor.fetchall()
            return registros

if __name__=="__main__":
    
    #Insertar
    #Contrato_personas = Contrato_persona(idpersona=2,idcontrato=2)
    #idInsertadas = Contrato_personaDao.insertar(Contrato_personas)
    #log.debug(f"Id insertadas {idInsertadas}")
    
    #Ver
    #contrato_personas = Contrato_personaDao.seleccionar()
    #for p in contrato_personas:
    #    log.debug(p)

    #Obtener Costos por Correo
    contrato_personas = Contrato_personaDao.costostotal(correo="morin@gmail.com")
    for p in contrato_personas:
        log.debug(f"COSTO TOTAL DE CONTRATOS ES DE: ${p}")

    #Descripción de contratos por correos
    contrato_personas = Contrato_personaDao.obtenercontrato(correo="morin@gmail.com")
    for p in contrato_personas:
        log.debug(p)
