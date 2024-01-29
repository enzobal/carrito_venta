"""
URL configuration for carrito project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf import settings
# from django.conf.urls.static import static

from CarritoApp.views import tienda, agregar_producto, eliminar_producto,restar_producto,limpiar_carrito, index
urlpatterns = [
   
    # path('', include('libreria.urls')),
    # path('inicio/', views.inicio, name='inicio'),
]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from CarritoApp.views import tienda, agregar_producto, eliminar_producto,restar_producto, limpiar_carrito, index, seguidores, yo, contactanos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tienda, name="Tienda"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('index/', index, name="index"),
    path('contactanos/', contactanos , name="contactanos"),
    path('seguidores/', seguidores, name="seguidores"), 
    path('conoceme/', yo, name="conoceme" )
]# Configuración para servir archivos multimedia durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
