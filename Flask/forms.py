from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EscuelaForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    direccion = StringField("Direccion", validators=[DataRequired()])
    enviar = SubmitField("Enviar datos")

class MaestroForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    enviar = SubmitField("Enviar datos")
    
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    enviar = SubmitField("Iniciar sesion")
