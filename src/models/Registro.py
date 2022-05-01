from ..extensions import db

class Registro(db.Model):
    __tablename__ = 'registros'
    PK_idRegistro = db.Column(db.Integer(), primary_key=True)
    FK_idUsuario = db.Column(db.Integer(), db.ForeignKey('usuairos.PK_idUsuairo',ondelte="CASCADE")) 
    FK_idEmpresa = db.Column(db.Decimal(), db.ForeignKey('empresas.PK_idEmpresa',ondelte="CASCADE"))