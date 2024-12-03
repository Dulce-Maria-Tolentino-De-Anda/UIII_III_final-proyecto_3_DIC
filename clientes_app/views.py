from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.
def inicio_vistaClientes(request):
    losclientes = Cliente.objects.all()
    return render(request, "gestionarClientes.html", {"misclientes": losclientes})

def registrarCliente(request):
    id_cliente = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    email = request.POST["txtemail"]
    telefono = request.POST["txttelefono"]
    direccion = request.POST["txtdireccion"]
    fecha_registro = request.POST["txtfecha"]
    historial_compras = request.POST["txthistorial"]

    Cliente.objects.create(
        id_cliente=id_cliente,
        nombre=nombre,
        email=email,
        telefono=telefono,
        direccion=direccion,
        fecha_registro=fecha_registro,
        historial_compras=historial_compras,
    )

    return redirect("clientes")

def seleccionarCliente(request, codigo):
    cliente = Cliente.objects.get(id_cliente=codigo)
    fecha_registro=cliente.fecha_registro.strftime('%Y-%m-%d')
    return render(request,"editarCliente.html",{"misclientes":cliente, "misclientes" : cliente, "fecha_registro" : fecha_registro})

def editarCliente(request):
    id_cliente = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    email = request.POST["txtemail"]
    telefono = request.POST["txttelefono"]
    direccion = request.POST["txtdireccion"]
    fecha_registro = request.POST["txtfecha"]
    historial_compras = request.POST["txthistorial"]

    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre = nombre
    cliente.email = email
    cliente.telefono = telefono
    cliente.direccion = direccion
    cliente.fecha_registro = fecha_registro
    cliente.historial_compras = historial_compras
    cliente.save()

    return redirect("clientes")

def borrarCliente(request, codigo):
    cliente = Cliente.objects.get(id_cliente=codigo)
    cliente.delete()
    return redirect("clientes")
