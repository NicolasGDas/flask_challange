# from flask import Flask
# from config import config
# from errors import errors as er
# from api import views
# from api import routes
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# db = SQLAlchemy(app)


# class Empresa(db.Model):
#     __tablename__ = 'empresas'
#     PK_idEmpresa = db.Column(db.Integer(), primary_key=True)

# def crear_modelo_empresa(db):
#     class Usuario(db.Model):
#         __tablename__ = 'usuarios'
#         PK_idUsuario = db.Column(db.Integer(), primary_key=True)
#         FK_idEMpresa = db.Column(db.Integer(), db.ForeignKey('empresas.PKidEMpresa'))


# @app.route('/cargar_registro',methods=["POST"])
# def cargar_registro():
#     return views.cargar_registro()


# @app.route('/balance_empresa',methods=["GET"])
# def get_balance_empresa():
#     return views.get_balance_empresa()


# @app.route('/balance_empresa_usuario',methods=["GET"])
# def get_balance_empresa_usuario():
#     return views.get_balance_empresa_usuario()




# if __name__ == '__main__':
#     app.config.from_object(config['development'])
#     app.register_error_handler(404, er.pagina_no_encontrada)
#     app.run()

