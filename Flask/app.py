import json
import logging
from flask import Flask, abort, request, url_for, render_template, redirect, session, flash, jsonify
from database import db
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from models import Escuela, Maestro, Alumno, Materia, Evento
from forms import EscuelaForm, MaestroForm, LoginForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
bootstrap = Bootstrap5(app)

logging.basicConfig(filename='flask_logger.log', level=logging.DEBUG)



# Configurar la db
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'escuela'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.config['BOOTSTRAP_BTN_STYLE'] = 'primary'
app.config['BOOTSTRAP_BTN_SIZE'] = 'sm'

db.init_app(app)


# Configurar migracion
migrate = Migrate()
migrate.init_app(app, db)

csrf = CSRFProtect()
csrf.init_app(app)

# Secret key
app.config['SECRET_KEY'] = "llaveexamen12345"

@app.errorhandler(404)
def appErrorHandler(error):
    return render_template('/default/error.html', error=error), 404


@app.before_request
def middleware():
    login_url = url_for('login')
    
    d = [url_for('eventos'), url_for('alumnos'), url_for('materias')]
    
    if request.path == login_url:
        return
    elif not session.get('logged_in', False) and request.path not in d :
        return redirect(login_url)

@app.route('/logout')
def logout():
    if session:
        session.pop('logged_in')
    return redirect(url_for('login'))

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('logged_in', False):
        return redirect(url_for('inicio'))
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        username = loginForm.username.data
        session['logged_in'] = True
        session['username'] = username
        return redirect(url_for('inicio'))
    return render_template('login.html',form=loginForm)


@app.route("/inicio")
def inicio():
    return render_template('/inicio/index.html')


##################################
    # RUTAS #
##################################
## ESCUELA ##

@app.route("/escuelas")
def escuelas():
    if not session.get('logged_in', False):
        return redirect(url_for('login'))
    escuelas = Escuela.query.all()
    return render_template('/escuela/index.html', escuelas=escuelas)

@app.route("/escuelas/agregar", methods=['GET', 'POST'])
def agregarEscuela():
    escuela = Escuela()
    escuelaForm = EscuelaForm(obj=escuela)
    if request.method == 'POST':
        if escuelaForm.validate_on_submit():
            escuelaForm.populate_obj(escuela)
            # Insert a la db
            db.session.add(escuela)
            db.session.commit()
            return redirect(url_for('escuelas'))
    return render_template('/escuela/agregar.html', forma = escuelaForm)

@app.route("/escuelas/<int:id>/editar", methods=['GET', 'POST'])
def editarEscuela(id):
    escuela = Escuela.query.get_or_404(id)
    escuelaForm = EscuelaForm(obj=escuela)
    if request.method == 'POST':
        if escuelaForm.validate_on_submit():
            escuelaForm.populate_obj(escuela)
            #Update a la db, no es necesario hacer nada mas.
            db.session.commit()
            return redirect(url_for('escuelas'))
    return render_template('/escuela/editar.html', forma = escuelaForm)

@app.route("/escuelas/<int:id>/eliminar")
def eliminarEscuela(id):
    escuela = Escuela.query.get_or_404(id)
    db.session.delete(escuela)
    db.session.commit()
    return redirect(url_for('escuelas'))

## FIN ESCUELA ##

## RUTAS MAESTRO ##


@app.route("/maestros")
def maestros():
    if not session.get('logged_in', False):
        return redirect(url_for('login'))
    maestros = Maestro.query.all()
    return render_template('/maestro/index.html', maestros=maestros)

@app.route("/maestro/agregar", methods=['GET', 'POST'])
def agregarMaestro():
    maestro = Maestro()
    maestroForm = MaestroForm(obj=maestro)
    if request.method == 'POST':
        if maestroForm.validate_on_submit():
            maestroForm.populate_obj(maestro)
            # Insert a la db
            db.session.add(maestro)
            db.session.commit()
            return redirect(url_for('maestros'))
    return render_template('/maestro/agregar.html', forma = maestroForm)

@app.route("/maestros/<int:id>/editar", methods=['GET', 'POST'])
def editarMaestro(id):
    maestro = Maestro.query.get_or_404(id)
    maestroForm = MaestroForm(obj=maestro)
    if request.method == 'POST':
        if maestroForm.validate_on_submit():
            maestroForm.populate_obj(maestro)
            #Update a la db, no es necesario hacer nada mas.
            db.session.commit()
            return redirect(url_for('maestros'))
    return render_template('/maestro/editar.html', forma = maestroForm)

@app.route("/maestros/<int:id>/eliminar")
def eliminarMaestro(id):
    maestro = Maestro.query.get_or_404(id)
    db.session.delete(maestro)
    db.session.commit()
    return redirect(url_for('maestros'))



## FIN MAESTRO ##




## RUTAS ALUMNO ##
@app.route('/alumnos')
def alumnos():
    return render_template('/alumno/index.html')
## FIN ALUMNO ##


## RUTAS MATERIA ##
@app.route('/materias')
def materias():
    return render_template('/materia/index.html')
## FIN MATERIA ##


## RUTAS EVENTO ##
@app.route('/eventos')
def eventos():
    return render_template('/evento/index.html')
## FIN EVENTO ##



###################################

## RUTAS ESPECIALES PUNTO 7 EXAMEN ##

@app.route('/listaMaestros')
def getMaestros():
    maestros = Maestro.query.all()
    return jsonify(maestros) 

@app.route('/listaEscuelas')
def getEscuelas():
    escuelas = Escuela.query.all()
    return jsonify(escuelas) 

@app.route('/escuelas/findById/<int:id>')
def getEscuelaByID(id):
    escuela = Escuela.query.filter_by(id=id).first()
    if not escuela:
        return jsonify({'message': 'Escuela no encontrada', 'data': None})
    else:
        return jsonify({'message': 'Escuela encontrada exitosamente', 'data': escuela})

####################################

# Shortcuts

# flog -> debug rapido
# frt -> Render temprate rapido
# route -> ruta rapida

 
# Shortcuts jinja

# hbs4 -> boostrap js y html en corto




# Correr codigo = flask db init = crear carpetas proyecto
# Empezar migraciones = flask db migrate = crear tabla default
# Hacer migraciones = flask db upgrade = actualizar
# Instalar formas = pip install flask-wtf