from app.app import app
from flask import render_template
from flask_controller import FlaskController


class FacturacionController(FlaskController):
    @app.route('/facturacion.html')
    def facturacion():
        return render_template('facturacion.html')