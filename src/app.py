
from flask import Flask,request, send_file
from config import config
from db import consultas_db as db
from errors import errors as er
from common import funciones_common as common

app = Flask(__name__)



@app.route('/cargar_registro',methods=["POST"])
def cargar_registro():
    # variable usada para indicar que hubo un error
    had_error = False

    if request.method == "POST":
        # valido primero que me ingrese los 3 datos que necesito, asi tiro error antes de hacer cualquier cosa
        if request.form.get("idUsuario"):
            if request.form.get("idEmpresa"):
                if request.form.get("cantHA"):
                    idUsuario = request.form.get("idUsuario")
                    idEmpresa = request.form.get("idEmpresa")
                    cantHA = request.form.get("cantHA")

                    if not db.existe_usuario(idUsuario):
        #               No Existe el usuario, por ende lo tengo que crear
                        db.add_user_db(idUsuario)
                        #Verifico si la empresa existe o no
                        if not db.existe_empresa(idEmpresa):
                            #La empresa no existe, la creo
                            db.add_empresa_db(idEmpresa)
                        # le agrego al usuario la empresa correspondiente.
                        db.add_empresa_into_user(idUsuario,idEmpresa)
                    else:
                        #aca me tengo que fijar que la empresa sea la misma
                        if not db.es_misma_empresa(idUsuario,idEmpresa):
                            #la empresa no es la misma, retorno msj de error
                            #Aca podriamos hacer 2 cosas en realidad, decirle al usuario que esta mal lo que ingreso
                            #o Podriamos ignorar lo que el usuario ingreso y utilizar el valor de la db.
                            #Preferi decirle que valide los datos ingresados para no asumir nada de negocio
                            return er.error_en_empresa()
                    #creo un registro y lo agrego a la base de datos.
                    db.add_registro(idUsuario,idEmpresa,cantHA)
                else:
                    had_error,variable_faltante = True, "cantHA"
            else:
                had_error,variable_faltante = True,"idEmpresa"
        else:
            had_error,variable_faltante = True,"idUsuario"

    #esta validacion es para saber si tengo que mandar un error y poder mandarle
    #que variable no ingreso
    if had_error:
        return er.error_en_valores(variable_faltante)


    return er.datos_recibidos()


@app.route('/balance_empresa',methods=["GET"])
def get_balance_empresa():
    #devolverme en archivo json todos los registros de una misma empresa
    try:   
        if "idEmpresa" in request.args:
            idEmpresa = request.args["idEmpresa"]
            if idEmpresa != "":
            # me fijo si existe la empresa
                if db.existe_empresa(idEmpresa):
                    data = db.registros_por_empresa(idEmpresa)
                    if len(data) == 0:
                        return "Placeholder esta empresa no tiene registros"
                    #Formateo la data para poder enviarla como descargable    
                    balance = common.format_data_for_download(data)    
                else:
                    return "Placeholder ingrese valor"
            else:
                return er.error_no_existe("Empresa")
        else:
            return er.error_en_parametro("idEmpresa")
        
        
        return send_file(balance,download_name="descarga.json", as_attachment=True)
    except Exception as ex:
        return str(ex) 


@app.route('/balance_empresa_usuario',methods=["GET"])
def get_balance_empresa_usuario():
    # Recibo por parametro idUsuario e idEmpresa
    try:
        if "idEmpresa" in request.args:
            print(request.args["idEmpresa"])
            if request.args["idEmpresa"] != "":
                idEmpresa = request.args["idEmpresa"]
                if "idUsuario" in request.args:
                    if request.args["idUsuario"] != "":
                        idUsuario = request.args["idUsuario"]
                        if db.existe_empresa(idEmpresa):
                            #existe empresa
                            if db.existe_usuario(idUsuario):
                                #existe usuario
                                data = db.registros_empresa_usuario(idEmpresa,idUsuario)
                                if len(data) == 0:
                                    return "Placeholder esta empresa_usuario no tienen registros"
                                #Formateo la data para poder enviarla como descargable
                                balance = common.format_data_for_download(data)   
                                    
                            else:
                                return er.error_no_existe("Usuario") 
                        else:
                            return er.error_no_existe("Empresa")
                    else:
                        return er.error_en_parametro("idUsuario")
                else:
                    return er.error_en_parametro("idUsuario")
            else:
                return er.error_en_parametro("idEmpresa")
        else:
            return er.error_en_parametro("idEmpresa")

        return send_file(balance,download_name="descarga.json", as_attachment=True)
    except Exception as ex:
        return str(ex) 








if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, er.pagina_no_encontrada)
    app.run()