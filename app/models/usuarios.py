from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from app.models import session, Base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

class Usuarios(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, )
    fecha_nacimiento = Column(Date())
    cedula = Column(String(20), unique=True, nullable=False)
    telefono = Column(String(11))
    email = Column(String(20))
    area = Column(String(20))
    contraseña = Column(String(30), nullable=False)

   

    def __init__(self,nombre,fecha_nacimiento,cedula,telefono,email,area,contraseña): 
    
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.cedula = cedula
        self.telefono = telefono
        self.email = email
        self.area = area
        self.set_password(contraseña)

    def crear_usuario(usuario):
        usuario = session.add(usuario)
        session.commit()
        return usuario

    def traer_usuarios():
        usuarios = session.query(Usuarios).all()
        return usuarios

    def set_password(self, contraseña):
        self.contraseña = generate_password_hash(contraseña)

    def check_password(self, contraseña):
        return check_password_hash(self.contraseña, contraseña)