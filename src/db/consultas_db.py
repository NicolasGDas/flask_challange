from src.db import querys



"""
Funcion que recibe un idUsuario y lo busca en la db
retorna True en caso de encontrar el usuario en la db
retorna False en caso de que el usuario no exista ne la db
"""
def existe_usuario(idUsuario):
    datos = querys.query_obtener_usuario(idUsuario)
    if datos:
        return True
    return False


"""
Funcion que recibe un idEmpresa y lo busca en la db
retorna True en caso de encontrar el empresa en la db
retorna False en caso de que el empresa no exista ne la db
"""
def existe_empresa(idEmpresa):
    retorno = False
    datos = querys.query_obtener_empresa(idEmpresa)
    if datos:
        retorno  = True
    return retorno
"""
Funcion que recibe idUsuario y el posible idEmpresa
Busca  al usuario por el id y verifica si el idEmpesa ingresado es el mismo que esta
guardado en la db
Retorna True en caso de que el idEmpresa ingresado sea el mismo que en la db
Retorna False en caso de que el idEmpresa ingresado NO sea el mismo que la db
"""
def es_misma_empresa(idUsuario,idEmpresa):
    retorno = False
    datos = querys.query_obtener_usuario(idUsuario)
    if int(datos[0][1]) == int(idEmpresa):
        retorno  = True
    return retorno
"""
Esta funcion recibe el ide de la empresa, busca todos los registros de esa empresa
retorna una lista vacia si no hay registros o un dict con los datos en caso de 
tener registros
"""
def registros_por_empresa(idEmpresa):
    data ={}
    datos = querys.query_registros_por_empresa(idEmpresa)
    if len(datos) > 0:
        data[f"Empresa numero {idEmpresa}"] = []
        registro = {}
        for dato in datos:
                registro = {
                    "Usuario": dato[2],
                    "Cantidad HA": str(dato[3]) + " Hectareas" 
                }
                data[f"Empresa numero {idEmpresa}"].append(registro)
    else:
        data = []
    return data
"""
funcion que recibe una empresa y un usuario (su id)
Y busca los registros que cumplan que tengan el ambos id correspondientes
retorna una lista vacia si no hay registros o un dict con los datos en caso de 
tener registros
"""
def registros_empresa_usuario(idEmpresa,idUsuario):

    datos = querys.query_registro_por_empresa_usuario(idUsuario,idEmpresa)
    data ={}
    if len(datos) > 0:
        data[f"Empresa numero {idEmpresa}"] = []
        registro = {}
        for dato in datos:
                registro = {
                    "Usuario": dato[2],
                    "Cantidad HA": str(dato[3]) + " Hectareas" 
                }
                data[f"Empresa numero {idEmpresa}"].append(registro)
    else:
        data = []

    return data


def add_user_db(idUsuario):
    querys.add_user(idUsuario)
    

def add_empresa_db(idEmpresa):
    querys.add_empresa_db(idEmpresa)
    
def add_empresa_into_user(idUsuario,idEmpresa):
    querys.add_empresa_into_user(idUsuario,idEmpresa)
    

def add_registro(idUsuario,idEmpresa,cantHA):
    querys.add_registro(idUsuario,idEmpresa,cantHA)
