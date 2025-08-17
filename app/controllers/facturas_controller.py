from flask import render_template, request, redirect, url_for, flash
from app.app import app
from app.models.facturas import Facturas, DetalleFactura
from app.models.clientes import Clientes
from app.models.productos import Productos
from app.models import session
from datetime import datetime

class FacturasController:
    @app.route('/facturas', methods=['GET'])
    def listar_facturas():
        facturas = Facturas.traer_facturas()
        return render_template('/lista_facturas.html', facturas=facturas)

    @app.route('/facturas/nueva', methods=['GET', 'POST'])
    def crear_factura():
        if request.method == 'POST':
            try:
                
                factura_data = {
                    'numero_factura': request.form['numero_factura'],
                    'cliente_id': request.form['cliente_id']
                }
                factura = Facturas.crear_factura(factura_data)
                return redirect(url_for('agregar_items_factura', factura_id=factura.id))
            except Exception as e:
                flash(f'Error al crear factura: {str(e)}', 'error')
        
        clientes = Clientes.traer_clientes()
        return render_template('/nueva_factura.html', clientes=clientes)

    @app.route('/facturas/<int:factura_id>/items', methods=['GET', 'POST'])
    def agregar_items_factura(factura_id):
        factura = Facturas.factura_por_id(factura_id)
        
        if request.method == 'POST':
            try:
                detalle_data = {
                    'factura_id': factura_id,
                    'producto_id': request.form['producto_id'],
                    'cantidad': int(request.form['cantidad'])
                }
                DetalleFactura.agregar_detalle(detalle_data)
                flash('Item agregado correctamente', 'success')
            except ValueError as e:
                flash(str(e), 'error')
            except Exception as e:
                flash(f'Error al agregar item: {str(e)}', 'error')
        
        productos = Productos.traer_productos()
        return render_template('agregar_items.html', 
                             factura=factura, 
                             productos=productos)

    @app.route('/facturas/<int:factura_id>/eliminar-item/<int:detalle_id>', methods=['POST'])
    def eliminar_item_factura(factura_id, detalle_id):
        try:
            DetalleFactura.eliminar_detalle(detalle_id)
            flash('Item eliminado correctamente', 'success')
        except Exception as e:
            flash(f'Error al eliminar item: {str(e)}', 'error')
        return redirect(url_for('agregar_items_factura', factura_id=factura_id))

    @app.route('/facturas/<int:factura_id>/finalizar', methods=['POST'])
    def finalizar_factura(factura_id):
        factura = Facturas.factura_por_id(factura_id)
        if not factura.detalles:
            flash('No puede finalizar una factura sin items', 'error')
            return redirect(url_for('agregar_items_factura', factura_id=factura_id))
        
        factura.estado = 'Pagada'
        session.commit()
        return redirect(url_for('ver_factura', factura_id=factura_id))

    @app.route('/facturas/<int:factura_id>', methods=['GET'])
    def ver_factura(factura_id):
        factura = Facturas.factura_por_id(factura_id)
        return render_template('/ver_factura.html', factura=factura)

    @app.route('/facturas/<int:factura_id>/anular', methods=['POST'])
    def anular_factura(factura_id):
        factura = Facturas.factura_por_id(factura_id)
        
        
        for detalle in factura.detalles:
            producto = Productos.producto_por_id(detalle.producto_id)
            producto.cantidad_stock += detalle.cantidad
        
        factura.estado = 'Anulada'
        session.commit()
        
        return redirect(url_for('ver_factura', factura_id=factura_id))