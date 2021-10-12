from functools import partial
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrar-contacto/', views.registrarContacto),
    path('editar-contacto/', views.editarContacto),
    path('edicion-contacto/<cod>', views.edicionContacto),
    path('eliminar-contacto/<cod>', views.eliminarContacto)
]