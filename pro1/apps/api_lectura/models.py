from app import db
from sqlalchemy import Column, String, Integer, Float, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship


class Medidas(db.Model):
    __tablename__ = 'Medidas'

    id = Column(Integer, primary_key=True)
    numero_sensor = relationship('Sensor')
    v1 = Column(Float)
    v2 = Column(Float)
    v3 = Column(Float)
    v13 = Column(Float)
    v12 = Column(Float)
    v23 = Column(Float)
    i1 = Column(Float)
    i2 = Column(Float)
    i3 = Column(Float)
    p1 = Column(Float)
    p2 = Column(Float)
    p3 = Column(Float)
    pa = Column(Float)
    fp = Column(Float)
    hz = Column(Float)

    def __init__(self, numero_sensor, v1, v2, v3, v13, v12, v23, i1, i2, i3, p1, p2, p3, pa, fp, hz):
        sensor = self.numero_sensor
        v1 = self.v1
        v2 = self.v2
        v3 = self.v3
        v13 = self.v13
        v12 = self.v12
        v23 = self.v23
        i1 = self.i1
        i2 = self.i2
        i3 = self.i3
        p1 = self.p1
        p2 = self.p2
        p3 = self.p3
        pa = self.pa
        fp = self.fp
        hz = self.hz

    def __repr__(self):
        mediaLN = (self.v1 + self.v2 + self.v3) / 3
        mediaLL = (self.v13 + self.v12 + self.v23) / 3
        mediaI = (self.i1 + self.i2 + self.i3) / 3
        mediaP = (self.p1 + self.p2 + self.p3) / 3
        return f'Sensor: {self.sensor} - mediaLN: {mediaLN} - mediaLL: {mediaLL} - mediaI: {mediaI} - mediaP: {mediaP} - PA: {self.pa} - FP: {self.fp} - HZ: {self.hz}'


class Sensor(db.Model):
    __tablename__ = 'Sensor'

    id = Column(Integer, primary_key=True)
    numero_sensor = Column(Integer)
    numero_sensor_id = Column(Integer, ForeignKey('Medidas.id'))
    equipo = relationship('Equipo')
    ubicación = Column(String(64))

    def __init__(self, numero_sensor):
        numero_sensor = self.numero_sensor

    def __repr__(self) -> str:
        return f'Sensor N°: {self.numero_sensor} - {self.equipo}'


class Equipo(db.Model):
    __tablename__ = 'Equipo'

    id = Column(Integer, primary_key=True)
    marca = Column(String(32))
    modelo = Column(String(32))
    modelo_id = Column(Integer, ForeignKey('Sensor.id'))
    image = Column(LargeBinary, nullable=True)

    def __init__(self, marca, modelo, image):
        marca = self.marca
        modelo = self.modelo
        image = self.image

    def __repr__(self) -> str:
        return f'Equipo: {self.marca} - Modelo: {self.modelo}'
