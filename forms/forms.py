from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Signup')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class UnitForm(FlaskForm):
    name = TextAreaField('name', validators=[DataRequired()])
    systemID = IntegerField('systemID', validators=[DataRequired()])
    userID = IntegerField('userID', validators=[DataRequired()])
    submit = SubmitField('Post')

class SystemForm(FlaskForm):
    name = TextAreaField('name', validators=[DataRequired()])
    userID = IntegerField('userID', validators=[DataRequired()])
    submit = SubmitField('Post')

class CropForm(FlaskForm):
    name = TextAreaField('name', validators=[DataRequired()])
    unitID = IntegerField('unitID', validators=[DataRequired()])
    submit = SubmitField('Post')
    
class SensorForm(FlaskForm):
    name = TextAreaField('name', validators=[DataRequired()])
    unitID = IntegerField('unitID', validators=[DataRequired()])
    submit = SubmitField('Post')