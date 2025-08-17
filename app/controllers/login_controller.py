from flask import render_template, request, session, redirect, url_for, flash
from flask_controller import FlaskController
from app.models.usuarios import Usuarios
from app.app import app 
from app.models import session, Base
from werkzeug.security import check_password_hash

class Logincontroller (FlaskController):
    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/login.html', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email')
            contraseña = request.form.get('contraseña')

            
            usuario = session.query(Usuarios).filter_by(email=email).first()

            if usuario and usuario.check_password(contraseña):
                session['user_id'] = usuario.id  
                flash('¡Inicio de sesión exitoso!', 'success')
                return redirect(url_for('index.html'))  
            else:
                flash('Correo o contraseña incorrectos', 'danger')

        return render_template('login.html')

    @app.route('/index.html')
    def dashboard():
        if 'user_id' not in session:
            return redirect(url_for('index.html'))
        return "¡Bienvenido al Dashboard!"  

    @app.route('/logout')
    def logout():
        session.pop('user_id', None)
        flash('Has cerrado sesión', 'info')
        return redirect(url_for('login'))

    if __name__ == '__main__':
        app.run(debug=True)