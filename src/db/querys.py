import pymysql

def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='my-secret-pw',
                                db='auravant-challange')
"""
Query generica que recibe el nombre de la pk, la tabla y el id,
devuelve el pk de la tabla, es mas que nada para 
comprobar que existe este id
"""
#LA verdad que recibas el nombre de la pk esta mal, pero necesitaba hacerlo
#generico, y es lo que se me ocurrio, tranquilamente puede no existir esta version generica
# lo cual seria lo mejor
def query_una_condition_obtener_pk(pk,tabla,idBuscar):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = f"SELECT {pk} FROM {tabla} WHERE {pk} = {idBuscar}"
        cursor.execute(sql)
        datos = cursor.fetchone()
    conexion.close()
    return datos


"""
Query generica que recibe el nombre de la pk, la tabla y el id,
devuelve TODOS los campos de la tabla con dicho id
"""
#LA verdad que recibas el nombre de la pk esta mal, pero necesitaba hacerlo
#generico, y es lo que se me ocurrio, tranquilamente puede no existir esta version generica
# lo cual seria lo mejor
def query_una_condition_obtener_todo(pk,tabla,idBuscar):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = f"SELECT * FROM {tabla} WHERE {pk} = {idBuscar}"
        cursor.execute(sql)
        datos = cursor.fetchone()
    conexion.close()
    return datos


"""
Query generica que recibe el nombre de la  tabla dos tuplas para cada where,
las tuplas tienen que tener el formato (nombre_pk,pk)
devuelve TODOS los campos de la tabla que cumpla con ambos where
"""
def query_dos_conditions_obtener_todo(tabla,primerWhere,segundoWhere):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = f"SELECT * FROM {tabla} WHERE {primerWhere[0]} = {primerWhere[1]} AND {segundoWhere[0]} = {segundoWhere[1]}"
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