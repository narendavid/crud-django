from django.shortcuts import redirect, render
from .models import Contacto

# Create your views here.


def home(req):
    contactos = Contacto.objects.all()
    return render(req, "contactos.html", {"contactos": contactos})


def registrarContacto(req):
    codigo = req.POST['txtCodigo']
    nombre = req.POST['txtNombre']
    apellidos = req.POST['txtApellidos']
    email = req.POST['txtEmail']
    tel = req.POST['numTelefono']

    contacto = Contacto.objects.create(
        codigo=codigo, nombre=nombre, apellidos=apellidos, email=email, telefono=tel)
    return redirect('/')

def edicionContacto(req, cod):
    contacto = Contacto.objects.get(codigo = cod)
    return render(req, "editar.html", {"contacto": contacto})

def editarContacto(req):
    codigo = req.POST['txtCodigo']
    nombre = req.POST['txtNombre']
    apellidos = req.POST['txtApellidos']
    email = req.POST['txtEmail']
    tel = req.POST['numTelefono']
    contacto = Contacto.objects.get(codigo=codigo)
    contacto.nombre = nombre
    contacto.apellidos = apellidos
    contacto.email = email
    contacto.telefono = tel
    contacto.save()
    return redirect('/')

def eliminarContacto(req, cod):
    contacto = Contacto.objects.get(codigo = cod)
    contacto.delete()
    return redirect('/')