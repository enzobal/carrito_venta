# from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render, HttpResponse,redirect
# # Create your views here.
from CarritoApp.Carrito import Carrito
from CarritoApp.models import Producto
# # def inicio(request):
# #     return HttpResponse("<h1> Bienvenidos <h1>")


def tienda(request):
    # return HttpResponse("weeeep")
    productos =  Producto.objects.all()
    return render(request, "tienda.html", {'productos' :productos})

def agregar_producto(request, producto_id):
    carrito= Carrito(request)
    producto = Producto.objects.get(id=producto-id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto= Producto.object.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito= Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")
