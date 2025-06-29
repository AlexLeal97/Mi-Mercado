from sqlalchemy import Column, Integer, String
from app.models import session, Base

class Categorias(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    nombre_categoria = Column(String(300), unique=True, nullable=False)

    def __init__(self, nombre_categoria):
            self.nombre_categoria = nombre_categoria