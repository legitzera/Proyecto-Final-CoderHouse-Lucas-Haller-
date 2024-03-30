from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('saludo/', saludar),
    path('parametro/<nombre>', parametro),
    path('html/', html_hoy),
    path('tpl/', ejemplo_template),
    path('tpl_mejor/', ejemploMejor),
    path('nuevo_curso/', nuevo_curso),
    #-----------------------------LO DE ARRIBA FUE PRACTICA------------------------------------------
    path('', home, name="home"),
    path('creador/', creador, name="creador"),
    #-----------------------------CARTAS------------------------------------------
    path('cartas/', cartas, name="cartas"),
    path('carta_create/', cartaCreate, name="carta_create"),
    path('carta_update/<id_carta>/', cartaUpdate, name="carta_update"),
    path('buscar_cartas/', buscar_cartas, name="buscar_cartas"),
    path('encontrar_cartas/', encontrar_cartas, name="encontrar_cartas"),
    path('carta_delete/<id_carta>/', cartaDelete, name="carta_delete"),
    #-----------------------------DIBUJOS------------------------------------------
    path('dibujos/', dibujos, name="dibujos"),
    path('dibujo_create/', dibujoCreate, name="dibujo_create"),
    path('dibujo_update/<id_dibujo>/', dibujoUpdate, name="dibujo_update"),
    path('buscar_dibujos/', buscar_dibujos, name="buscar_dibujos"),
    path('encontrar_dibujos/', encontrar_dibujos, name="encontrar_dibujos"),
    path('dibujo_delete/<id_carta>/', dibujoDelete, name="dibujo_delete"),
    #-----------------------------FIGURAS------------------------------------------
    path('figuras/', figuras, name="figuras"),
    path('figura_create/', figuraCreate, name="figura_create"),
    path('figura_update/<id_figura>/', figuraUpdate, name="figura_update"),
    path('buscar_figuras/', buscar_figuras, name="buscar_figuras"),
    path('encontrar_figuras/', encontrar_figuras, name="encontrar_figuras"),
    #-----------------------------CAMISETAS------------------------------------------
    path('camisetas/', camisetas, name="camisetas"),
    path('camiseta_create/', camisetaCreate, name="camiseta_create"),
    path('camiseta_update/<id_camiseta>/', camisetaUpdate, name="camiseta_update"),
    path('buscar_camisetas/', buscar_camisetas, name="buscar_camisetas"),
    path('encontrar_camisetas/', encontrar_camisetas, name="encontrar_camisetas"),
    path('camiseta_delete/<id_camiseta>/', camisetaDelete, name="camiseta_delete"),
    #---------------Login , Logout, Registration ----------------------------------
    path('login/', login_request, name="login"),
    path('logout/', logout_request, name="logout"),
    path('registrar/', register, name="registrar"),
    #---------------Edicion perfil, Cambio de clave, Avatar ----------------------------------
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]