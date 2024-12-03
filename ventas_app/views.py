from django.shortcuts import render, redirect
from .models import Ventas

def inicio_vistaVentas(request):
    las_ventas = Ventas.objects.all()
    return render(request, "gestionarVentas.html", {"mis_ventas": las_ventas})

def registrarVenta(request):
    id_venta = request.POST["txtcodigo"]
    id_empleado = request.POST["numidempleado"]
    id_producto = request.POST["numidproducto"]
    id_cliente = request.POST["numidcliente"]
    fecha_venta = request.POST["datefecha_venta"]
    cantidad = request.POST["numcantidad"]
    total = request.POST["numtotal"]

    Ventas.objects.create(
        id_venta=id_venta, id_empleado=id_empleado, id_producto=id_producto,
        id_cliente=id_cliente, fecha_venta=fecha_venta, cantidad=cantidad, total=total
    )
    return redirect("ventas")

def seleccionarVenta(request, codigo):
    venta = Ventas.objects.get(id_venta=codigo)
    fecha_venta = venta.fecha_venta.strftime('%Y-%m-%d')
    return render(request, "editarVenta.html", {"mi_venta": venta, "fecha_venta": fecha_venta})

def editarVenta(request):
    id_venta = request.POST["txtcodigo"]
    id_empleado = request.POST["numidempleado"]
    id_producto = request.POST["numidproducto"]
    id_cliente = request.POST["numidcliente"]
    fecha_venta = request.POST["datefecha_venta"]
    cantidad = request.POST["numcantidad"]
    total = request.POST["numtotal"]

    venta = Ventas.objects.get(id_venta=id_venta)
    venta.id_empleado = id_empleado
    venta.id_producto = id_producto
    venta.id_cliente = id_cliente
    venta.fecha_venta = fecha_venta
    venta.cantidad = cantidad
    venta.total = total
    venta.save()
    return redirect("ventas")

def borrarVenta(request, codigo):
    venta = Ventas.objects.get(id_venta=codigo)
    venta.delete()
    return redirect("ventas")
