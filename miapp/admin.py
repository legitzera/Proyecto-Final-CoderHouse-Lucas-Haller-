from django.contrib import admin

# Register your models here.
from .models import *

class CartaAdmin(admin.ModelAdmin):
    list_display = ("nombre","tipo","precio_USD")

class DibujoAdmin(admin.ModelAdmin):
    list_display = ("nombre","autor","precio_USD")

class FiguraAdmin(admin.ModelAdmin):
    list_display = ("nombre","material","precio_USD")

class CamisetaAdmin(admin.ModelAdmin):
    list_display = ("nombre","color","forma", "precio_USD")        

admin.site.register(Dibujo, DibujoAdmin)
admin.site.register(Figura, FiguraAdmin)
admin.site.register(Carta, CartaAdmin)
admin.site.register(Camiseta, CamisetaAdmin)