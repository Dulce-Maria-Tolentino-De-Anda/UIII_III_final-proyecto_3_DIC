from django.urls import path
from empleados_app import views

urlpatterns = [
    path("empleados", views.inicio_vistaEmpleados, name="empleados"),
    path("registrarEmpleado/", views.registrarEmpleado, name="registrarEmpleado"),
    path("seleccionarEmpleado/<codigo>", views.seleccionarEmpleado, name="seleccionarEmpleado"),
    path("editarEmpleado/", views.editarEmpleado, name="editarEmpleado"),
    path("borrarEmpleado/<codigo>", views.borrarEmpleado, name="borrarEmpleado"),
]
