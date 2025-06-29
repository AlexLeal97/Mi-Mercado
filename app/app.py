from flask import Flask
from flask_controller import FlaskControllerRegister
from app.models import Base, engine




app = Flask(__name__)

register_controllers = FlaskControllerRegister(app)
register_controllers.register_package('app.controllers')

Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True)






   














