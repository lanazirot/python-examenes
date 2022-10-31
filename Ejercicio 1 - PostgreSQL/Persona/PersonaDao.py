import sys        
sys.path.append('C:/Examen - Postgresql')
from Persona import Persona
from Conexion import Conexion
from CursorDelPool import CursorDelPool
from logger_base import log

class PersonaDao:
    _SELECCIONAR = "SELECT * FROM persona ORDER BY idpersona"
    _INSERTAR = "INSERT INTO persona(nombre,edad,correo) Values(%s,%s,%s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s,edad=%s,correo=%s WHERE idpersona=%s"
    _ELIMINAR = "DELETE FROM persona WHERE idpersona=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas=[]
                for r in registros:
                    persona = Persona(r[0],r[1],r[2],r[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls,Persona):
        with CursorDelPool() as cursor:
            valores = (Persona.nombre, Persona.edad, Persona.correo)
            cursor.execute(cls._INSERTAR,valores)
            log.debug("Se registro la persona")
            return cursor.rowcount

    @classmethod
    def actualizar(cls,Persona):
        with CursorDelPool() as cursor:
            valores = (Persona.nombre, Persona.edad, Persona.correo, Persona.idpersona)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug("Se actualizo la persona")
            return cursor.rowcount

    @classmethod
    def eliminar(cls,Persona):
        with CursorDelPool() as cursor:
            valores = (Persona.idpersona,)
            cursor.execute(cls._ELIMINAR,valores)
            log.debug("Se elimino la persona")
            return cursor.rowcount

if __name__=="__main__":
    
    #Insertar
    #personas = Persona(idpersona=1,nombre="Carlos",edad="18",correo="morin@gmail.com")
    #personasInsertadas = PersonaDao.insertar(personas)
    #log.debug(f"Personas insertadas {personasInsertadas}")
    
    #Actualizar
    #persona1=Persona(idpersona=2,nombre="Miguel",edad="19",correo="miguel@gmail.com")
    #personasActualizadas = PersonaDao.actualizar(persona1)
    #log.debug(f"Personas actualizadas {personasActualizadas}")
    
    #Eliminar
    #persona1=Persona(idpersona=3)
    #personasEliminadas = PersonaDao.eliminar(persona1)
   #log.debug(f"Personas eliminadas {personasEliminadas}")
    
    #Ver
    personas = PersonaDao.seleccionar()
    for p in personas:
        log.debug(p)