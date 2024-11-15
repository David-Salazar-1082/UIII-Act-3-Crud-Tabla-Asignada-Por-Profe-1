from django.shortcuts import render,redirect
from .models import Producto

# Create your views here.

def inicio_vista(request):
    losproductos=Producto.objects.all()
    return render(request, 'gestionarProducto.html', {'productos': losproductos})


def registrarProducto(request):
    Id_Producto =request.POST['txtId_Producto']
    Precio =request.POST['txtPrecio']
    Marca =request.POST['txtMarca']
    Calidad =request.POST['txtCalidad']
    Recibido =request.POST['txtRecibido']
    Proovedor =request.POST['txtProovedor']
    Cantidad =request.POST['txtCantidad']

    registrarProducto =Producto.objects.create(Id_Producto=Id_Producto, Precio=Precio, Marca=Marca, Calidad=Calidad, Recibido=Recibido, Proovedor=Proovedor, Cantidad=Cantidad)
    return redirect('/')
    
def seleccionarProducto(request,Id_Producto):
    producto=Producto.objects.get(Id_Producto=Id_Producto)
    return render(request,"editarproducto.html",{"misproductos":producto})

def editarProducto(request):
    Id_Producto =request.POST['txtId_Producto']
    Precio =request.POST['txtPrecio']
    Marca =request.POST['txtMarca']
    Calidad =request.POST['txtCalidad']
    Recibido =request.POST['txtRecibido']
    Proovedor =request.POST['txtProovedor']
    Cantidad =request.POST['txtCantidad']
    producto=Producto.objects.get(Id_Producto=Id_Producto)
    producto.Precio=Precio
    producto.Marca=Marca
    producto.Calidad=Calidad
    producto.Recibido=Recibido
    producto.Proovedor=Proovedor
    producto.Cantidad=Cantidad
    
    producto.save()
    return redirect('/')

def borrarProducto(request,Id_Producto):
    producto=Producto.objects.get(Id_Producto=Id_Producto)
    producto.delete()
    return redirect('/')