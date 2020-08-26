from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Environment(db.Model):
    __tablename__ = "sensordata_db"
    id = db.Column(db.Integer, primary_key=True)
    airtemp = db.Column(db.Integer, nullable=False)
    airhumidity = db.Column(db.Integer, nullable=False)
    watertemp = db.Column(db.Integer, nullable=False)

class System(db.Model):
    __tablename__ = "systems"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    units = db.relationship('Unit', backref='sys')

class Sensor(db.Model):
    __tablename__ = "sensors"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    unitid = db.Column(db.Integer, db.ForeignKey('units.id'))
    name = db.Column(db.String(64), nullable=False)

class Unit(db.Model):
    __tablename__ = "units"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    systemid = db.Column(db.Integer, db.ForeignKey('systems.id'), nullable=False)
    sensorid = db.Column(db.Integer, db.ForeignKey('sensors.id'), nullable=False)
    
    # date_started = db.Column(db.String(64), nullable=False)
    # performance = db.Column(db.String(64), nullable=False)

class Crop(db.Model):
    __tablename__ = "crops"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)