from db import db

class Datos(db.Model):

    __tablename__="datos"

    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    lat=db.Column(db.Float)
    lng=db.Column(db.Float)
    des=db.Column(db.String(100))

    def __init__(self, nombre, lat, lng, des):  

        self.nombre=nombre
        self.lat=lat
        self.lng=lng
        self.des=des
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'lat': self.lat,
            'lng': self.lng,
            'des': self.des
        }
