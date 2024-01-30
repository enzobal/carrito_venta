from django.contrib import admin 
#usuario piru contrseña 1234    56
from .models import Producto

from .models import Producto2
# Register your models here.

# producto3 es de index
from .models import Producto3


admin.site.register(Producto)
admin.site.register(Producto2)
admin.site.register(Producto3)
