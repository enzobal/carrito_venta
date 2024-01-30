# from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render, HttpResponse,redirect
# # Create your views here.
from CarritoApp.Carrito import Carrito
from CarritoApp.models import Producto
from CarritoApp.models import Producto2
from CarritoApp.models import Producto3
from CarritoApp.context_processor import  total_carrito
# # def inicio(request):
# #     return HttpResponse("<h1> Bienvenidos <h1>")

def index(request):
    productos3 =  Producto3.objects.all()  
    return render(request, "index.html",{'productos' :productos3} )

def seguidores(request):
    productos2 =  Producto2.objects.all()
    return render(request, "seguidores.html", {'productos' :productos2})

def tienda(request):
    
    productos =  Producto.objects.all()    
    return render(request, "tienda.html", {'productos' :productos})

def contactanos(request):
    return render(request, "contactanos.html", )




def yo(request):
    return render(request, "yo.html", )

def agregar_producto(request, producto_id):
    carrito= Carrito(request)
    producto = Producto.objects.get(id=producto_id)
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
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito= Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")



# def total(request):
#     # Lógica para calcular el total de los productos
#     total = sum(producto.precio for producto in producto)
#     return render(request, 'tienda.html', {'productos': producto, 'total': total})


