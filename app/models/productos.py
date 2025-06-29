from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.models import session, Base
from app.models.categorias import Categorias

class Productos(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    codigo = Column(String(9), unique=True, nullable=False)
    descripcion = Column(String(300), unique=True, nullable=False)
    valor_unitario = Column(Float)
    unidad_medida = Column(String(3), nullable=False)
    cantidad_stock = Column(Integer)
    categoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)

    def __init__(self,codigo,descripcion,valor_unitario,unidad_medida,cantidad_stock,categoria):
        self.codigo = codigo
        self.descripcion = descripcion
        self.valor_unitario = valor_unitario
        self.unidad_medida = unidad_medida
        self.cantidad_stock = cantidad_stock
        self.categoria = categoria

    def crear_producto(producto):
        producto = session.add(producto)
        session.commit()
        return producto

    def traer_productos():
        productos =  session.query(Productos).all()
        return productos
