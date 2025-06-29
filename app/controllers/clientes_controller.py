

from flask import render_template, request
from flask_controller import FlaskController
from app.models.clientes import Clientes
from app.app import app

class ClientesController(FlaskController):
    @app.route('/formulario_cliente.html', methods=['GET', 'POST'])
    def formulario_cliente():

        if request.method == 'POST':
                nombre = request.form.get('nombre')
                fecha_nacimiento = request.form.get('fecha_nacimiento')
                cedula = request.form.get('cedula')
                telefono = request.form.get('telefono')        
                email = request.form.get('email')
                cliente = Clientes(nombre,fecha_nacimiento,cedula,telefono,email,)
                Clientes.crear_cliente(cliente)
        return render_template('formulario_cliente.html', titulo='Ver productos')

    @app.route('/clientes.html', methods = ['GET','POST'])
    def clientes():
        clientes = Clientes.traer_clientes()
        return render_template('clientes.html',titulo='Ver productos', clientes = clientes)