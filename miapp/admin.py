from django.contrib import admin

# Register your models here.
from .models import *

class CartaAdmin(admin.ModelAdmin):
    list_display = ("nombre","tipo")

class DibujoAdmin(admin.ModelAdmin):
    list_display = ("nombre","autor")

admin.site.register(Dibujo, DibujoAdmin)
admin.site.register(Figura)
admin.site.register(Carta, CartaAdmin)