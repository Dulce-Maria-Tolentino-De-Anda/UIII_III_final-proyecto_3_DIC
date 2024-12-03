from django.urls import path
from clientes_app import views

urlpatterns = [
    path("clientes", views.inicio_vistaClientes, name="clientes"),
    path("registrarCliente/", views.registrarCliente, name="registrarCliente"),
    path("seleccionarCliente/<codigo>", views.seleccionarCliente, name="seleccionarCliente"),
    path("editarCliente/", views.editarCliente, name="editarCliente"),
    path("borrarCliente/<codigo>", views.borrarCliente, name="borrarCliente"),
]
