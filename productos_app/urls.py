from django.urls import path
from productos_app import views

urlpatterns = [
    path("productos", views.inicio_vistaProductos, name="productos"),
    path("registrarProducto/", views.registrarProducto, name="registrarProducto"),
    path("seleccionarProducto/<codigo>", views.seleccionarProducto, name="seleccionarProducto"),
    path("editarProducto/", views.editarProducto, name="editarProducto"),
    path("borrarProducto/<codigo>", views.borrarProducto, name="borrarProducto"),
]
