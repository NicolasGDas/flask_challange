from ..extensions import db


class Empresa(db.Model):
    __tablename__ = 'empresas'
    PK_idEmpresa = db.Column(db.Integer(), primary_key=True)