from app.utils.db import db
from sqlalchemy.dialects.postgresql import psycopg2


class Usuario(db.Model):
    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Identificacion = db.Column(db.String(20))
    Contraseña = db.Column(db.String(255), nullable=False)
    Rol = db.Column(db.String(50), nullable=False)


    def __init__(self, identificacion, contraseña, rol):

        self.Identificacion = identificacion
        self.Contraseña = contraseña
        self.Rol = rol

    @property
    def obtenerDatos(self):
        return {
            'UserID': self.UserID,
            'Identificacion': self.Identificacion,
            'Contraseña': self.Contraseña,
            'Rol': self.Rol
        }