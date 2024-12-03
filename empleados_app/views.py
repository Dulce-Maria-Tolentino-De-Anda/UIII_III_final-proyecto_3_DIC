from django.shortcuts import render, redirect
from .models import Empleado

def inicio_vistaEmpleados(request):
    los_empleados = Empleado.objects.all()
    return render(request, "gestionarEmpleados.html", {"mis_empleados": los_empleados})

def registrarEmpleado(request):
    id_empleado = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    apellidos = request.POST["txtapellidos"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["numtelefono"]
    email = request.POST["txtemail"]
    fecha_nacimiento = request.POST["datefecha_nacimiento"]

    Empleado.objects.create(
        id_empleado=id_empleado, nombre=nombre, apellidos=apellidos,
        direccion=direccion, telefono=telefono, email=email,
        fecha_nacimiento=fecha_nacimiento
    )
    return redirect("empleados")

def seleccionarEmpleado(request, codigo):
    empleado = Empleado.objects.get(id_empleado=codigo)
    fecha_nacimiento = empleado.fecha_nacimiento.strftime('%Y-%m-%d')
    return render(request, "editarEmpleado.html", {"mi_empleado": empleado, "fecha_nacimiento": fecha_nacimiento})

def editarEmpleado(request):
    id_empleado = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    apellidos = request.POST["txtapellidos"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["numtelefono"]
    email = request.POST["txtemail"]
    fecha_nacimiento = request.POST["datefecha_nacimiento"]

    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.nombre = nombre
    empleado.apellidos = apellidos
    empleado.direccion = direccion
    empleado.telefono = telefono
    empleado.email = email
    empleado.fecha_nacimiento = fecha_nacimiento
    empleado.save()
    return redirect("empleados")

def borrarEmpleado(request, codigo):
    empleado = Empleado.objects.get(id_empleado=codigo)
    empleado.delete()
    return redirect("empleados")
