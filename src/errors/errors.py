from src.templates import templates
""""
Funciones que retornan el template con la data necesaria para manejar errores

"""
#podria ser mas que errores -> generar_templates o algo asi
def error_no_existe(item):
    return templates.no_existe(item)
    
def error_en_parametro(param):
    return templates.bad_req_param(param)

def error_en_valores(string):
    return templates.bad_req(string)

def datos_recibidos():
    return templates.todo_ok()
def error_en_empresa():
    return templates.mal_empresa()

def pagina_no_encontrada(self):
    return templates.pagina_no_encontrada()

def no_registro(query):
    return templates.no_registro(query)