from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from app.models import User, db

auth = Blueprint('auth', __name__)

# Ruta para el login (GET y POST)
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))  # Si ya está autenticado, redirige

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Buscar usuario en la base de datos
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)  # Inicia sesión
            flash('¡Inicio de sesión exitoso!', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Correo o contraseña incorrectos.', 'danger')
    
    return render_template('login.html')

# Ruta para cerrar sesión
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('auth.login'))

# Ruta protegida (ejemplo)
@auth.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)