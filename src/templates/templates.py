def todo_ok():
    return "<h1>Todo Ok</h1>", 200

def pagina_no_encontrada():
    return "<h1>Página no encontrada</h1>", 404

def bad_req(problem):
    return f"<h1>Por favor, no se encontro la variable:  {problem}, por favor ingresela</h1>", 400

def bad_req_param(problem):
    return f"<h1>Por favor, no se encontro el parametro:  {problem}, por favor ingreselo</h1>", 400

def mal_empresa():
    return f"<h1>La empresa ingresada no tiene ese usuario, verificar datos ingresados</h1>", 400

def no_existe(problem):
    return f"<h1>No existe:  {problem}, con ese id, verificar datos ingresados</h1>", 400

def no_registro(query):
    return f"<h1>La query:  {query}, no tienen registros guardados</h1>", 400