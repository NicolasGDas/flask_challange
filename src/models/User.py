from ..extensions import db




class Usuario(db.Model):
    __tablename__ = 'usuarios'
    PK_idUsuario = db.Column(db.Integer(), primary_key=True)
    FK_idEMpresa = db.Column(db.Integer(), db.ForeignKey('empresas.PKidEMpresa',ondelete = "CASCADE"))
