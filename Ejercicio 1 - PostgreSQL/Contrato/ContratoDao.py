import sys        
sys.path.append('C:/Examen - Postgresql')
from Contrato import Contrato
from Conexion import Conexion
from CursorDelPool import CursorDelPool
from logger_base import log

class ContratoDao:
    _SELECCIONAR = "SELECT * FROM contrato ORDER BY idcontrato"
    _INSERTAR = "INSERT INTO contrato(numcontrato,costo,fechainicio,fechafin) Values(%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE contrato SET numcontrato=%s,costo=%s,fechainicio=%s, fechafin=%s WHERE idcontrato=%s"
    _ELIMINAR = "DELETE FROM contrato WHERE idcontrato=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                contratos=[]
                for r in registros:
                    contrato = Contrato(r[0],r[1],r[2],r[3],r[4])
                    contratos.append(contrato)
                return contratos

    @classmethod
    def insertar(cls,Contrato):
        with CursorDelPool() as cursor:
            valores = (Contrato.numcontrato, Contrato.costo, Contrato.fechainicio, Contrato.fechafin)
            cursor.execute(cls._INSERTAR,valores)
            log.debug("Se registro el contrato")
            return cursor.rowcount

    @classmethod
    def actualizar(cls,Contrato):
        with CursorDelPool() as cursor:
            valores = (Contrato.numcontrato, Contrato.costo, Contrato.fechainicio, Contrato.fechafin, Contrato.idcontrato)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug("Se actualizo el contrato")
            return cursor.rowcount

    @classmethod
    def eliminar(cls,Contrato):
        with CursorDelPool() as cursor:
            valores = (Contrato.idcontrato,)
            cursor.execute(cls._ELIMINAR,valores)
            log.debug("Se elimino el contrato")
            return cursor.rowcount

if __name__=="__main__":
    
    #Insertar
    #contratos = Contrato(idcontrato=1,numcontrato="001",costo=1000,fechainicio="12 de Abril 2022",fechafin="30 de Abril 2023")
    #contratosInsertados = ContratoDao.insertar(contratos)
    #log.debug(f"Contratos insertados {contratosInsertados}")
    
    #Actualizar
    contrato1=Contrato(idcontrato=2,numcontrato="011",costo=1500,fechainicio="13 de Mayo 2021",fechafin="30 de Mayo 2022")
    contratosActualizados = ContratoDao.actualizar(contrato1)
    log.debug(f"Contratos actualizados {contratosActualizados}")
    
    #Eliminar
    #contrato1=Contrato(idcontrato=3)
    #contratosEliminados = ContratoDao.eliminar(contrato1)
    #log.debug(f"Contratos eliminados {contratosEliminados}")
    
    #Ver
    #contratos = ContratoDao.seleccionar()
    #for p in contratos:
    #    log.debug(p)