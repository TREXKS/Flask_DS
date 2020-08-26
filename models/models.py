from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    units = db.relationship('Unit', backref='user_units')
    systems = db.relationship('System', backref='user_systems')

    def get_id(self):
        return (self.uid)

class Sensor_Info(db.Model):
    __tablename__ = "sensor_info"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    unit = db.Column(db.String(64), nullable=False)
    manufacturer = db.Column(db.String(64), nullable=False)        

class Crop_Info(db.Model):
    __tablename__ = "crop_info"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    soil = db.Column(db.String(200), nullable=False)
    position = db.Column(db.String(200), nullable=False)
    frost = db.Column(db.String(200), nullable=False)
    feeding = db.Column(db.String(200), nullable=False)
    companions = db.Column(db.String(200), nullable=False)
    spacing = db.Column(db.String(200), nullable=False)
    sow = db.Column(db.String(200), nullable=False)
    notes = db.Column(db.String(200), nullable=False)       
    harvesting = db.Column(db.String(200), nullable=False)
    troubleshooting = db.Column(db.String(200), nullable=False)   

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
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'))

class Unit(db.Model):
    __tablename__ = "units"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    system_id = db.Column(db.Integer, db.ForeignKey('systems.id'))
    crops = db.relationship('Crop', backref='crp')
    sensors = db.relationship('Sensor', backref='sns')
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'))

class Crop(db.Model):
    __tablename__ = "crops"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'))

class Sensor(db.Model):
    __tablename__ = "sensors"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'))    
