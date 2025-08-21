from sqlalchemy import Column, Integer, String
from app.models import session, Base

class Categorias(Base):
    __tablename__ = "categorias"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)
    descripcion = Column(String(200))
    
    def __init__(self, nombre, descripcion=None):
        self.nombre = nombre
        self.descripcion = descripcion
    
    @classmethod
    def traer_todas(cls):
        return session.query(cls).order_by(cls.nombre).all()
    
    @classmethod
    def obtener_por_id(cls, id):
        return session.query(cls).get(id)