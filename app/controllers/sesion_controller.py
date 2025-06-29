from app.app import app
from flask import render_template
from flask_controller import FlaskController


class HomeController(FlaskController):
    @app.route('/')
    def inicio_sesion():
        return render_template('inicio_sesion.html')
    
    @app.route('/inicio_sesion.html')
    def cerrar_sesion():
        return render_template('inicio_sesion.html')