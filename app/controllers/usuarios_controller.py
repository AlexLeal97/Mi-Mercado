from flask import render_template, request
from flask_controller import FlaskController
from app.models.usuarios import Usuarios
from app.app import app


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
    
    @app.route('/eliminar_usuario/<int:usuario_id>', methods=['POST'])
    def eliminar_usuario(usuario_id):
        if Usuarios.eliminar_usuario(usuario_id):
            return {'success': True, 'message': 'Usuario eliminado correctamente'}, 200
        return {'success': False, 'message': 'Usuario no encontrado'}, 404
    
    @app.route('/editar_usuario.html')
    def editar_usuario():
        return render_template('editar_usuario.html')