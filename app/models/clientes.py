from sqlalchemy import Column, Integer, String, Float, ForeignKey,Date
from app.models import session, Base

class Clientes(Base):
    __tablename__ = "clientes"
    id_cliente = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, )
    fecha_nacimiento = Column(Date())
    cedula = Column(String(20), unique=True, nullable=False)
    telefono = Column(String(20))
    email = Column(String(20))

    def __init__(self,nombre,fecha_nacimiento,cedula,telefono,email):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.cedula = cedula
        self.telefono = telefono
        self.email = email
        
    def crear_cliente(cliente):
        cliente = session.add(cliente)
        session.commit()
        return cliente
    
    def traer_clientes():
        clientes = session.query(Clientes).all()
        return clientes
