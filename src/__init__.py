from flask import Flask
from .errors import errors as er
from .api.routes import api
from .config import DATABASE_CONNECTION_URI
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(api)
    app.register_error_handler(404, er.pagina_no_encontrada)
    

    return app
