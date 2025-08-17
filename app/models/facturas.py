from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import session, Base
from app.models.clientes import Clientes
from app.models.productos import Productos

class Facturas(Base):
    __tablename__ = "facturas"
    id = Column(Integer, primary_key=True)
    numero_factura = Column(String(20), unique=True, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    total = Column(Float, default=0.0)
    estado = Column(String(20), default='Pendiente')  
    
    
    cliente = relationship("Clientes", backref="facturas")
    detalles = relationship("DetalleFactura", backref="factura", cascade="all, delete-orphan")

    def __init__(self, numero_factura, cliente_id):
        self.numero_factura = numero_factura
        self.cliente_id = cliente_id

    @classmethod
    def crear_factura(cls, factura_data):
        factura = cls(
            numero_factura=factura_data['numero_factura'],
            cliente_id=factura_data['cliente_id']
        )
        session.add(factura)
        session.commit()
        return factura

    @classmethod
    def traer_facturas(cls):
        return session.query(cls).all()

    @classmethod
    def factura_por_id(cls, factura_id):
        return session.query(cls).get(factura_id)

    def calcular_total(self):
        self.total = sum(detalle.subtotal for detalle in self.detalles)
        session.commit()
        return self.total

class DetalleFactura(Base):
    __tablename__ = "detalle_factura"
    id = Column(Integer, primary_key=True)
    factura_id = Column(Integer, ForeignKey('facturas.id'), nullable=False)
    producto_id = Column(Integer, ForeignKey('productos.id'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)
    
 
    producto = relationship("Productos")

    def __init__(self, factura_id, producto_id, cantidad, precio_unitario):
        self.factura_id = factura_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = cantidad * precio_unitario

    @classmethod
    def agregar_detalle(cls, detalle_data):
        producto = Productos.producto_por_id(detalle_data['producto_id'])
        
       
        if producto.cantidad_stock < detalle_data['cantidad']:
            raise ValueError("Stock insuficiente")
        
        detalle = cls(
            factura_id=detalle_data['factura_id'],
            producto_id=detalle_data['producto_id'],
            cantidad=detalle_data['cantidad'],
            precio_unitario=producto.valor_unitario
        )
        
        
        producto.cantidad_stock -= detalle_data['cantidad']
        
        session.add(detalle)
        session.commit()
        
        
        factura = Facturas.factura_por_id(detalle_data['factura_id'])
        factura.calcular_total()
        
        return detalle

    @classmethod
    def eliminar_detalle(cls, detalle_id):
        detalle = session.query(cls).get(detalle_id)
        if detalle:
            
            producto = Productos.producto_por_id(detalle.producto_id)
            producto.cantidad_stock += detalle.cantidad
            
            factura_id = detalle.factura_id
            session.delete(detalle)
            session.commit()
            
            
            factura = Facturas.factura_por_id(factura_id)
            factura.calcular_total()
            
        return detalle
    
