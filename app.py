# set FLASK_APP=app.py
# set FLASK_ENV=development
# flask run

import csv
import os

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session, abort, g

from flask_login import LoginManager, login_user

from models.models import *
from forms.forms import *
from passlib.hash import sha256_crypt


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

# Set up database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:#######@localhost:5432/sensordata_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "s14a-key"
db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')
    

# DASHBOARD PAGES

@app.route('/dashboard')
def dashboard():
    
    all_systems = System.query.all()
    all_units = Unit.query.all()
    all_crops = Crop.query.all()

    system_count = len(all_systems)
    unit_count = len(all_units)
    crop_count = len(all_crops)

    return render_template('dashboard.html', all_systems=all_systems, all_units=all_units, system_count=system_count, unit_count=unit_count, crop_count=crop_count )

# POST ROUTES

@app.route('/unitpost', methods=['GET', 'POST'])
def unitpost():
    # Init form
    form = UnitForm()

    # If POST
    if request.method == 'POST':

        # Init user from poster

        # Init content from form request
        name = request.form['name']
        systemID = request.form['systemID']
        userID = request.form['userID']

        # Create in DB
        new_post = Unit(name=name, system_id=systemID, user_id=userID)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('units'))

    # If GET
    else:
        return render_template('units.html', title='unitpost', form=form)

@app.route('/systempost', methods=['GET', 'POST'])
def systempost():
    # Init form
    form = SystemForm()

    # If POST
    if request.method == 'POST':

        # Init user from poster

        # Init content from form request
        name = request.form['name']
        userID = request.form['userID']

        # Create in DB
        new_post = System(name=name, user_id=userID)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('systems'))

    # If GET
    else:
        return render_template('system.html', title='systempost', form=form)

@app.route('/croppost', methods=['GET', 'POST'])
def croppost():
    # Init form
    form = CropForm()

    # If POST
    if request.method == 'POST':

        # Init user from poster

        # Init content from form request
        name = request.form['name']
        unitID = request.form['unitID']

        # Create in DB
        new_post = Crop(name=name, unit_id=unitID)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('crops'))

    # If GET
    else:
        return render_template('crop.html', title='croppost', form=form)


@app.route('/sensorpost', methods=['GET', 'POST'])
def sensorpost():
    # Init form
    form = SensorForm()

    # If POST
    if request.method == 'POST':

        # Init user from poster
        # session_user = User.query.filter_by(username=session['username']).first()

        # Init content from form request
        name = request.form['name']
        unitID = request.form['unitID']

        # Create in DB
        new_post = Sensor(name=name, unit_id=unitID)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('sensors'))

    # If GET
    else:
        return render_template('sensor.html', title='sensorpost', form=form)

# PAGE ROUTES

@app.route('/systems')
def systems():
    form = SystemForm()

    all_systems = System.query.all()

    return render_template('systems.html', all_systems=all_systems, form=form)

@app.route('/units')
def units():
    form = UnitForm()

    all_units = Unit.query.all()
    all_systems = System.query.all()

    return render_template('units.html', all_units=all_units, all_systems=all_systems, form=form)

@app.route('/sensors')
def sensors():
    form = SensorForm()

    all_sensors = Sensor.query.all()

    return render_template('sensors.html', all_sensors=all_sensors, form=form)

@app.route('/crops')
def crops():
    form = CropForm()

    all_crops = Crop.query.all()

    return render_template('crops.html', all_crops=all_crops, form=form)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/support')
def support():
    return render_template('support.html')


# ACCOUNT MANAGEMENT

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Init form
    form = LoginForm()

    # If post
    if request.method == 'POST':

        # Init credentials from form request
        username = request.form['username']
        password = request.form['password']

        # Init user by Db query
        user = User.query.filter_by(username=username).first()

        # Control login validity
        if user is None or not sha256_crypt.verify(password, user.password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:
            login_user(user)
            next = request.args.get('next')
            return redirect(next or url_for('dashboard'))

    # If GET
    else:
        return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Init form
    form = SignupForm()

    # IF POST
    if request.method == 'POST':

        # Init credentials from form request
        username = request.form['username']
        password = request.form['password']

        # Init user from Db query
        existing_user = User.query.filter_by(username=username).first()

        # Control new credentials
        if existing_user:
            flash('The username already exists. Please pick another one.')
            return redirect(url_for('register'))
        else:
            user = User(username=username, password=sha256_crypt.hash(password))
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))

    # IF POST
    else:
        return render_template('register.html', title='Signup', form=form)
    
#POST /logout
@app.route('/logout', methods=['POST', 'GET'])
def logout():
    # Logout
    session.clear()
    return redirect(url_for('index'))