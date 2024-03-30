from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.urls import reverse_lazy

import datetime
import random

from miapp.models import *
from miapp.forms import *

from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def saludar (request):
    return render("Este es el mensaje de saludo")

def parametro (request, nombre):
    respuesta = f"Este es el mensaje de saludo con parametro: {nombre}"
    return render (respuesta)

def html_hoy (request):
    hoy = datetime.datetime.now()
    respuesta = f"""
    <html>
    <h1> Ejemplo con HTML </h1>
    <h2> h2 es para algo mas chico </h2>
    <h3> ejemplo de hoy es: {hoy} </h3>
    </html>
    """
    return render (respuesta) 

def ejemplo_template(request):
    miHtml = open("C:/Users/Usuario/Desktop/Programmer/PAG 1/ejemplo/ejemplo/plantillas/ejemplo.html")
    plantilla = Template(miHtml.read())
    miHtml.close ()
    contexto = Context()
    respuesta = plantilla.render(contexto)
    return render(respuesta)

def ejemploMejor(request):
    hoy = datetime.datetime.now()
    nombre = "legit"
    apellido = "zera"
    notas = [4,5,6,7,8,9]
    contexto = {"nombre" : nombre, "apellido" : apellido, "hoy" : hoy, "notas" : notas}
    plantilla = loader.get_template("ejemplomejor.html")
    respuesta = plantilla.render(contexto)
    return render(request, "miapp/ejemplomejor.html")

def nuevo_curso(rlogin_requiredequest):
    iComision = random.randint(20000,30000)
    sNombre = "Python " + str(iComision)
    curso = Curso(nombre=sNombre, comision=iComision)
    curso.save()
    respuesta = f"<html><h1>El curso nuevo es {sNombre} : {iComision}</h1></html>"
    return render(respuesta)

#-----------------------------LO DE ARRIBA FUE PRACTICA------------------------------------------

def home (request):
    return render(request, "miapp/index.html")

def creador (request):
    return render(request, "miapp/creador.html")

#-----------------------------CARTAS------------------------------------------
@login_required
def cartas (request):
    contexto = {'cartas' : Carta.objects.all().order_by("nombre")}
    return render(request, "miapp/cartas.html", contexto)

@login_required
def cartaCreate (request):
    if request.method == "POST":
        miForm = CartaForm(request.POST)
        if miForm.is_valid():
            carta_nombre = miForm.cleaned_data.get("nombre")
            carta_tipo = miForm.cleaned_data.get("tipo")
            carta_precio_USD = miForm.cleaned_data.get("precio_USD")
            carta = Carta(nombre=carta_nombre, tipo=carta_tipo, precio_USD=carta_precio_USD)
            carta.save()
            return redirect(reverse_lazy('cartas'))
    else:
        miForm = CartaForm()
    return render(request, "miapp/cartaForm.html", {"form": miForm})

@login_required
def cartaUpdate (request, id_carta):
    carta = Carta.objects.get(id=id_carta)
    if request.method == "POST":
        miForm = CartaForm(request.POST)
        if miForm.is_valid():
            carta.nombre = miForm.cleaned_data.get("nombre")
            carta.tipo = miForm.cleaned_data.get("tipo")
            carta.precio_USD = miForm.cleaned_data.get("precio_USD")
            carta.save()

            return redirect(reverse_lazy('cartas'))
    else:
        miForm = CartaForm(initial={'nombre': carta.nombre, 'tipo': carta.tipo, 'precio': carta.precio_USD})
    return render(request, "miapp/cartaForm.html", {"form": miForm})

@login_required
def buscar_cartas(request):
    return render(request, "miapp/buscar.html")

@login_required
def encontrar_cartas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        cartas = Carta.objects.filter(nombre__icontains=patron)
        contexto = {"cartas": cartas}
        return render(request, "miapp/cartas.html", contexto)
    
    contexto = {'cartas' : Carta.objects.all()}
    return render(request, "miapp/cartas.html", contexto)

@login_required
def cartaDelete (request, id_carta):
    carta = Carta.objects.get(id=id_carta)
    carta.delete()
    return redirect(reverse_lazy('cartas'))

#-----------------------------FIGURAS------------------------------------------
@login_required
def figuras (request):
    contexto = {'figuras' : Figura.objects.all().order_by("material")}
    return render(request, "miapp/figuras.html", contexto)

@login_required
def figuraCreate (request):
    if request.method == "POST":
        miForm = FiguraForm(request.POST)
        if miForm.is_valid():
            figura_nombre = miForm.cleaned_data.get("nombre")
            figura_material = miForm.cleaned_data.get("material")
            figura_precio_USD = miForm.cleaned_data.get("precio_USD")
            figura = Figura(nombre=figura_nombre, material=figura_material, precio_USD=figura_precio_USD)
            figura.save()
            return redirect(reverse_lazy('figuras'))
    else:
        miForm = FiguraForm()
    return render(request, "miapp/figuraForm.html", {"form": miForm})

@login_required
def figuraUpdate (request, id_figura):
    figura = Figura.objects.get(id=id_figura)
    if request.method == "POST":
        miForm = FiguraForm(request.POST)
        if miForm.is_valid():
            figura.nombre = miForm.cleaned_data.get("nombre")
            figura.material = miForm.cleaned_data.get("material")
            figura.precio_USD = miForm.cleaned_data.get("precio_USD")
            figura.save()

            return redirect(reverse_lazy('figuras'))
    else:
        miForm = FiguraForm(initial={'nombre': figura.nombre, 'material': figura.material, 'precio' : figura.precio_USD})
    return render(request, "miapp/figuraForm.html", {"form": miForm})

@login_required
def buscar_figuras(request):
    return render(request, "miapp/buscar_figuras.html")

@login_required
def encontrar_figuras(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        figuras = Figura.objects.filter(nombre__icontains=patron)
        contexto = {"figuras": figuras}
        return render(request, "miapp/figuras.html", contexto)
    
    contexto = {'figuras' : Figura.objects.all()}
    return render(request, "miapp/figuras.html", contexto)

@login_required
def figuraDelete (request, id_figura):
    figura = Figura.objects.get(id=id_figura)
    figura.delete()
    return redirect(reverse_lazy('figuras'))
#-----------------------------DIBUJOS------------------------------------------

@login_required
def dibujos (request):
    contexto = {'dibujos' : Dibujo.objects.all().order_by("autor")}
    return render(request, "miapp/dibujos.html", contexto)

@login_required
def dibujoCreate (request):
    if request.method == "POST":
        miForm = DibujoForm(request.POST)
        if miForm.is_valid():
            dibujo_nombre = miForm.cleaned_data.get("nombre")
            dibujo_autor = miForm.cleaned_data.get("autor")
            dibujo_precio_USD = miForm.cleaned_data.get("precio_USD")
            dibujo = Dibujo(nombre=dibujo_nombre, autor=dibujo_autor, precio_USD=dibujo_precio_USD)
            dibujo.save()
            return redirect(reverse_lazy('dibujos'))
    else:
        miForm = DibujoForm()
    return render(request, "miapp/dibujoForm.html", {"form": miForm})

@login_required
def dibujoUpdate (request, id_dibujo):
    dibujo = Dibujo.objects.get(id=id_dibujo)
    if request.method == "POST":
        miForm = DibujoForm(request.POST)
        if miForm.is_valid():
            dibujo.nombre = miForm.cleaned_data.get("nombre")
            dibujo.autor = miForm.cleaned_data.get("autor")
            dibujo.precio_USD = miForm.cleaned_data.get("precio_USD")
            dibujo.save()

            return redirect(reverse_lazy('dibujos'))
    else:
        miForm = DibujoForm(initial={'nombre': dibujo.nombre, 'autor': dibujo.autor, 'precio' : dibujo.precio_USD})
    return render(request, "miapp/dibujoForm.html", {"form": miForm})

@login_required
def buscar_dibujos(request):
    return render(request, "miapp/buscar_dibujos.html")

@login_required
def encontrar_dibujos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        dibujos = Dibujo.objects.filter(nombre__icontains=patron)
        contexto = {"dibujos": dibujos}
        return render(request, "miapp/dibujos.html", contexto)
    
    contexto = {'dibujos' : Dibujo.objects.all()}
    return render(request, "miapp/dibujos.html", contexto)

@login_required
def dibujoDelete (request, id_dibujo):
    dibujo = Dibujo.objects.get(id=id_dibujo)
    dibujo.delete()
    return redirect(reverse_lazy('dibujos'))

#-----------------------------REMERAS------------------------------------------
@login_required
def camisetas (request):
    contexto = {'camisetas' : Camiseta.objects.all().order_by("nombre")}
    return render(request, "miapp/camisetas.html", contexto)

@login_required
def camisetaCreate (request):
    if request.method == "POST":
        miForm = CamisetaForm(request.POST)
        if miForm.is_valid():
            camiseta_nombre = miForm.cleaned_data.get("nombre")
            camiseta_color = miForm.cleaned_data.get("color")
            camiseta_forma = miForm.cleaned_data.get("forma")
            camiseta_precio_USD = miForm.cleaned_data.get("precio_USD")
            camiseta = Camiseta(nombre=camiseta_nombre, color=camiseta_color, forma=camiseta_forma, precio_USD=camiseta_precio_USD)
            camiseta.save()
            return redirect(reverse_lazy('camisetas'))
    else:
        miForm = CamisetaForm()
    return render(request, "miapp/camisetaForm.html", {"form": miForm})

@login_required
def camisetaUpdate (request, id_camiseta):
    camiseta = Camiseta.objects.get(id=id_camiseta)
    if request.method == "POST":
        miForm = CamisetaForm(request.POST)
        if miForm.is_valid():
            camiseta.nombre = miForm.cleaned_data.get("nombre")
            camiseta.color = miForm.cleaned_data.get("color")
            camiseta.forma = miForm.cleaned_data.get("forma")
            camiseta.precio_USD = miForm.cleaned_data.get("precio_USD")
            camiseta.save()

            return redirect(reverse_lazy('camisetas'))
    else:
        miForm = CamisetaForm(initial={'nombre': camiseta.nombre, 'color': camiseta.color, 'forma': camiseta.forma, 'precio' : camiseta.precio_USD})
    return render(request, "miapp/cartaForm.html", {"form": miForm})

@login_required
def buscar_camisetas(request):
    return render(request, "miapp/buscar_camisetas.html")

@login_required
def encontrar_camisetas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        camisetas = Camiseta.objects.filter(nombre__icontains=patron)
        contexto = {"camiseta": camisetas}
        return render(request, "miapp/camisetas.html", contexto)
    
    contexto = {'camisetas' : Camiseta.objects.all()}
    return render(request, "miapp/camisetas.html", contexto)

@login_required
def camisetaDelete (request, id_camiseta):
    camiseta = Camiseta.objects.get(id=id_camiseta)
    camiseta.delete()
    return redirect(reverse_lazy('camisetas'))

#-----------------------------Login , Logout, Authentication, Registration --------
def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request,user)

            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            
            return render(request, "miapp/index.html")
        else:
            return redirect(reverse_lazy('login'))
            
    else:
        miForm = AuthenticationForm()
    return render(request, "miapp/login.html", {"form": miForm})

def logout_request(request):
    logout(request)
    
    return redirect('home')

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
   
        miForm = RegistroForm()

    return render(request, "miapp/registro.html", {"form": miForm} ) 

#-----------------------------EDICION, CAMBIO DE CLAVE, AVATAR ----------------
@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = UserEditForm(instance=usuario)

    return render(request, "miapp/editarPerfil.html", {"form": miForm} )

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "miapp/cambiar_clave.html"
    success_url = reverse_lazy("home")  

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
        miForm = AvatarForm()

    return render(request, "miapp/agregarAvatar.html", {"form": miForm} )     