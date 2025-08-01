from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from app.models import session, Base

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


    def __init__(self,id,nombre,fecha_nacimiento,cedula,telefono,email,area,contraseña): 
    
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.cedula = cedula
        self.telefono = telefono
        self.email = email
        self.area = area
        self.contraseña = contraseña

    def crear_usuario(usuario):
        usuario = session.add(usuario)
        session.commit()
        return usuario

    def traer_usuarios():
        usuarios = session.query(Usuarios).all()
        return usuarios

    @classmethod
    def eliminar_usuario(cls, usuario_id):
        """Elimina un usuario por su ID con manejo de errores"""
        try:
            usuario = session.query(cls).get(usuario_id)
            if not usuario:
                return False
                
            session.delete(usuario)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            print(f"Error al eliminar usuario: {str(e)}")
            return False