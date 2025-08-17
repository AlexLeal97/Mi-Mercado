
from flask import render_template, request, request, session, redirect, url_for
from flask_controller import FlaskController
from app.models.clientes import Clientes
from app.app import app
from app.models import session, Base

class ClientesController(FlaskController):
    @app.route('/formulario_cliente.html', methods=['GET', 'POST'])
    def formulario_cliente():

        if request.method == 'POST':
                nombre = request.form.get('nombre')
                fecha_nacimiento = request.form.get('fecha_nacimiento')
                cedula = request.form.get('cedula')
                telefono = request.form.get('telefono')        
                email = request.form.get('email')
                cliente = Clientes(nombre,fecha_nacimiento,cedula,telefono,email)
                Clientes.crear_cliente(cliente)
        return render_template('formulario_cliente.html', titulo='Ver productos')

    @app.route('/clientes.html', methods = ['GET','POST'])
    def clientes():
        clientes = Clientes.traer_clientes()
        return render_template('clientes.html',titulo='Ver productos', clientes = clientes)
    
    @app.route('/editar_cliente.html/<int:id>', methods=['GET', 'POST'])
    def editar_cliente(id):
        cliente = session.query(Clientes).get(id)
        
        if request.method == 'POST':
           
            cliente.codigo = request.form.get('nombre')
            cliente.descripcion = request.form.get('fecha_nacimiento')
            cliente.valor_unitario = request.form.get('cedula')
            cliente.cantidad_stock = request.form.get('telefono')
            cliente.unidad_medida = request.form.get('email')
            
           
            session.commit()
            
            return redirect(url_for('clientes'))
        
        return render_template('editar_cliente.html', 
                            titulo='Editar cliente', 
                            cliente=cliente)

    @app.route('/eliminar_cliente/<int:id>', methods=['POST'])
    def eliminar_cliente(id):
        cliente = session.query(Clientes).get(id)
        if cliente:
            session.delete(cliente)
            session.commit()
        return redirect(url_for('clientes'))