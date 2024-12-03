from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.
def inicio_vistaProductos(request):
    losproductos = Producto.objects.all()
    return render(request, "gestionarProducto.html", {"misproductos": losproductos})

def registrarProducto(request):
    id_producto = request.POST["txtcodigo"]
    modelo = request.POST["txtmodelo"]
    tipo_camara = request.POST["txttipo_camara"]
    precio = request.POST["txtprecio"]
    resolucion_mp = request.POST["txtresolucion"]
    fecha_agregada = request.POST["txtfecha"]

    Producto.objects.create(
        id_producto=id_producto,
        modelo=modelo,
        tipo_camara=tipo_camara,
        precio=precio,
        resolucion_mp=resolucion_mp,
        fecha_agregada=fecha_agregada,
    )

    return redirect("productos")

def seleccionarProducto(request, codigo):
    producto = Producto.objects.get(id_producto=codigo)
    fecha_agregada = producto.fecha_agregada.strftime('%Y-%m-%d')
    return render(request, "editarProducto.html", {"misproductos": producto, "fecha_agregada": fecha_agregada})

def editarProducto(request):
    id_producto = request.POST["txtcodigo"]
    modelo = request.POST["txtmodelo"]
    tipo_camara = request.POST["txttipo_camara"]
    precio = request.POST["txtprecio"]
    resolucion_mp = request.POST["txtresolucion"]
    fecha_agregada = request.POST["txtfecha"]

    producto = Producto.objects.get(id_producto=id_producto)
    producto.modelo = modelo
    producto.tipo_camara = tipo_camara
    producto.precio = precio
    producto.resolucion_mp = resolucion_mp
    producto.fecha_agregada = fecha_agregada
    producto.save()

    return redirect("productos")

def borrarProducto(request, codigo):
    producto = Producto.objects.get(id_producto=codigo)
    producto.delete()
    return redirect("productos")
