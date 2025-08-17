from flask import Flask
from flask_controller import FlaskControllerRegister
from app.models import Base, engine
from flask_login import LoginManager
from app.models.usuarios import Usuarios







app = Flask(__name__)
app.secret_key = 'leal.1997'

register_controllers = FlaskControllerRegister(app)
register_controllers.register_package('app.controllers')



login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader  
def load_user(user_id):
    return Usuarios.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)






   














