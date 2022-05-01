from flask import Blueprint
from src.errors import errors as er
from src.api import views

api = Blueprint('api',__name__,url_prefix='/api')


@api.route('/cargar_registro',methods=["POST"])
def cargar_registro():
    return views.cargar_registro()


@api.route('/balance_empresa',methods=["GET"])
def get_balance_empresa():
    return views.get_balance_empresa()


@api.route('/balance_empresa_usuario',methods=["GET"])
def get_balance_empresa_usuario():
    return views.get_balance_empresa_usuario()