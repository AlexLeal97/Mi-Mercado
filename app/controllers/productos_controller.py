from flask import render_template, request, session, redirect, url_for
from flask_controller import FlaskController
from app.models.productos import Productos
from app.app import app 
from app.models import session, Base

class ProductosController(FlaskController):
    @app.route('/formulario_producto.html', methods=['GET','POST'])
    def formulario_producto():
        if request.method == 'POST':
            codigo = request.form.get('codigo')
            descripcion = request.form.get('descripcion')
            valor_unitario = request.form.get('valor_unitario')
            cantidad_inventario = request.form.get('cantidad_inventario')        
            unidad_medida = request.form.get('unidad_medida')
            categoria = request.form.get('categoria')
            producto = Productos(codigo,descripcion,valor_unitario,unidad_medida,cantidad_inventario,categoria)
            Productos.crear_producto(producto)
            print ("Entró por POST")
            print(codigo)    
        return render_template('formulario_producto.html',titulo='Crear un producto')

    @app.route('/inventario.html' , methods= ['GET','POST'])
    def lista_productos():
        productos = Productos.traer_productos()
        return render_template('inventario.html',titulo='Ver productos', productos = productos)
    
    @app.route('/editar_producto/<int:id>', methods=['GET', 'POST'])
    def editar_producto(id):
        producto = session.query(Productos).get(id)
        
        if request.method == 'POST':
           
            producto.codigo = request.form.get('codigo')
            producto.descripcion = request.form.get('descripcion')
            producto.valor_unitario = request.form.get('valor_unitario')
            producto.cantidad_stock = request.form.get('cantidad_inventario')
            producto.unidad_medida = request.form.get('unidad_medida')
            producto.categoria = request.form.get('categoria')
            
           
            session.commit()
            
            return redirect(url_for('lista_productos'))
        
        return render_template('editar_producto.html', 
                            titulo='Editar Producto', 
                            producto=producto)

    @app.route('/eliminar_producto/<int:id>', methods=['POST'])
    def eliminar_producto(id):
        producto = session.query(Productos).get(id)
        if producto:
            session.delete(producto)
            session.commit()
        return redirect(url_for('lista_productos'))