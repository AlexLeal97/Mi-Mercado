from flask import render_template, request
from flask_controller import FlaskController
from app.models.productos import Productos
from app.app import app

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