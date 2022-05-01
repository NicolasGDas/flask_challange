import pymysql
from src.config import user,password,host,database
"""
Todas estas querys estan realizadas con pymsql porque fue con el que emprece, despues me pase a 
sqlalchemy porque era mas facil para intanciar la db. 
Si quisiera cambiar estos metodos quedarian obsoletos y deberia implementar con sqlAlchemy


"""
def obtener_conexion():
    return pymysql.connect(host=host,
                                user=user,
                                password=password,
                                db=database)

"""
Devuelve el idEmpresa de la tabla empresa
"""
def query_obtener_empresa(idEmpresa):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = f"SELECT * FROM empresas WHERE PK_idEmpresa = {idEmpresa}"
        cursor.execute(sql)
        datos = cursor.fetchall()
    conexion.close()
    return datos
"""
Funcion que devuelve todos los datos de un usuario
"""
def query_obtener_usuario(idUsuario):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = f"SELECT * FROM usuarios WHERE PK_idUsuario = {idUsuario}"
        cursor.execute(sql)
        datos = cursor.fetchall()
    conexion.close()
    return datos


"""

"""

#LA verdad que recibas el nombre de la pk esta mal, pero necesitaba hacerlo
#generico, y es lo que se me ocurrio, tranquilamente puede no existir esta version generica
# lo cual seria lo mejor
def query_registros_por_empresa(idEmpresa):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = f"SELECT * FROM registros WHERE FK_idEmpresa = {idEmpresa}"
        cursor.execute(sql)
        datos = cursor.fetchall()
    conexion.close()
    return datos


"""
Query generica que recibe el nombre de la  tabla dos tuplas para cada where,
las tuplas tienen que tener el formato (nombre_pk,pk)
devuelve TODOS los campos de la tabla que cumpla con ambos where
"""
def query_registro_por_empresa_usuario(idUsuario,idEmpresa):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = f"SELECT * FROM registros WHERE FK_idUsuario = {idUsuario} AND FK_idEmpresa = {idEmpresa}"
        cursor.execute(sql)
        datos = cursor.fetchall()
    conexion.close()
    return datos

"""
Funcion que añade usuarios a la db
"""

def add_user(idUsuario):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = f"INSERT INTO usuarios(PK_idUsuario) VALUES({idUsuario})"
        cursor.execute(sql)
    conexion.commit()
    conexion.close()

"""
Funcion que añade empresas a la db
"""
def add_empresa_db(idEmpresa):
    
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = f"INSERT INTO empresas(PK_idEmpresa) VALUES({idEmpresa})"
        cursor.execute(sql)
    conexion.commit()
    conexion.close()
"""
Funcion que añade empresas al usuario
"""
def add_empresa_into_user(idUsuario,idEmpresa):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = f"UPDATE  usuarios SET FK_idEmpresa = {idEmpresa} WHERE PK_idUsuario = {idUsuario}"
        cursor.execute(sql)
    conexion.commit()
    conexion.close()
    
"""
Funcion que crea registros en la db
"""
def add_registro(idUsuario,idEmpresa,cantHA):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = f"INSERT INTO registros(FK_idUsuario,FK_idEmpresa,cantHA) VALUES({idUsuario},{idEmpresa},{cantHA})"
        cursor.execute(sql)
    conexion.commit()
    conexion.close()