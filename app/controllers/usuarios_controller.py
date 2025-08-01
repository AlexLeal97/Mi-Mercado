from flask import render_template, request, redirect, session, redirect, url_for
from flask_controller import FlaskController
from app.models.usuarios import Usuarios
from app.app import app
from app.models import session, Base


class UsuariosController(FlaskController):
    @app.route('/formulario_usuario.html' ,methods=['GET','POST'])
    def crear_usuarios():
        
        if request.method == 'POST':
            nombre = request.form.get('nombre')
            fecha_nacimiento = request.form.get('fecha_nacimiento')
            cedula = request.form.get('cedula')
            telefono = request.form.get('telefono')        
            email = request.form.get('email')
            area = request.form.get('area')
            contraseña = request.form.get('contraseña')
            usuario = Usuarios(nombre,fecha_nacimiento,cedula,telefono,email,area,contraseña)
            Usuarios.crear_usuario(usuario)
            print ("Entró por POST")
            print(usuario)    
            
        return render_template('formulario_usuario.html', titulo='Ver productos')
    
    @app.route('/usuarios.html', methods=['GET', 'POST'])
    def usuarios():
        usuarios = Usuarios.traer_usuarios()
        return render_template('usuarios.html',titulo='Ver productos', usuarios = usuarios)
    

    @app.route('/editar_usuario.html/<int:id>', methods=['GET', 'POST'])
    def editar_usuario(id):
            usuario = session.query(Usuarios).get(id)
            
            if request.method == 'POST':
            
                usuario.nombre= request.form.get('nombre')
                usuario.fecha_nacimiento = request.form.get('fecha_nacimiento')
                usuario.cedula = request.form.get('cedula')
                usuario.telefono = request.form.get('telefono')
                usuario.email = request.form.get('email')
                usuario.area=request.form.get('area')
                usuario.contraseña = request.form.get('contraseña')
            
                session.commit()
                
                return redirect(url_for('usuarios'))
            
            return render_template('editar_usuario.html', 
                                titulo='Editar usuario', 
                                usuario = usuario)

    @app.route('/eliminar_usuario/<int:id>', methods=['POST'])
    def eliminar_usuario(id):
            usuario = session.query(Usuarios).get(id)
            if usuario:
                session.delete(usuario)
                session.commit()
            return redirect(url_for('usuarios'))
        
   