from django.http import HttpResponse
from django.shortcuts import render
from multiprocessing import context
from blog.forms import ArticuloForm, AutorForm, SeccionForm, UserEditForm, AvatarForm
from blog.models import Articulo, Autor, Seccion, Avatar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def mostrar_inicio(request):
    return HttpResponse("Bienvenidos al inicio")

def procesar_formulario_autor(request):
    if request.method == "GET":
        mi_formulario = AutorForm()
        contexto = {"formulario": mi_formulario}
        return render(request,"blog/formulario-autor.html", context=contexto)

    if request.method == "POST":
        mi_formulario = AutorForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo =Autor(
                nombre = datos_ingresados_por_usuario["nombre"],
                apellido = datos_ingresados_por_usuario["apellido"],
                profesion = datos_ingresados_por_usuario["profesion"],
            )
        nuevo_modelo.save()
        
        return render(request, "blog/exito.html")
    
    contexto = {"formulario":mi_formulario}
    return render(request,"blog/formulario-autor.html",context=contexto)

        
def procesar_formulario_articulo(request):
    if request.method == "GET":
        mi_formulario = ArticuloForm()
        contexto = {"formulario": mi_formulario}
        return render(request,"blog/formulario-articulo.html",context=contexto)
    
    if request.method == "POST":
        mi_formulario = ArticuloForm(request.POST)
       
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo =Articulo(
                titulo = datos_ingresados_por_usuario["titulo"],
                texto = datos_ingresados_por_usuario["texto"],
                fecha = datos_ingresados_por_usuario["fecha"],
            )   
        nuevo_modelo.save()
        
        return render(request, "blog/exito.html")
    
    contexto = {"formulario":mi_formulario}
    return render(request,"blog/formulario-articulo.html",context=contexto)

def procesar_formulario_seccion(request):
    if request.method == "GET":
        mi_formulario = SeccionForm()
        contexto = {"formulario": mi_formulario}
        return render(request,"blog/formulario-seccion.html",context=contexto)

    if request.method == "POST":
        mi_formulario = SeccionForm(request.POST)
        
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo =Seccion(
            titulo = datos_ingresados_por_usuario["titulo"],
        )
        nuevo_modelo.save()
        
        return render(request, "blog/exito.html")
    
    contexto = {"formulario":mi_formulario}
    return render(request,"blog/formulario-seccion.html",context=contexto)

        
def buscar(request):
    if  request.method == "GET":
        return render(request, "blog/formulario-de-busqueda.html")

    if request.method == "POST":
        titulo_para_buscar = request.POST["titulo"]
        resultados_de_busqueda = Articulo.objects.filter(titulo=titulo_para_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "blog/resultados-de-la-busqueda.html", context=contexto)




from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class AutorList(ListView):
    model = Autor
    template_name = "blog/autor_list.html"


class AutorDetalle(DetailView):
    model = Autor
    template_name = "blog/autor_detalle.html"


from django.urls import reverse 

class AutorCreate(CreateView):
    model = Autor
    fields = ["nombre", "apellido", "profesion"]
 
    def get_success_url(self):
        return reverse("AutorList")


class AutorUpdateView(UpdateView):
    model = Autor
    success_url = "/blog/autor/list"
    fields = ["nombre", "apellido", "profesion"]


class AutorDelete(DeleteView):
    model = Autor
    success_url = "/blog/autor/list"
    
class MyLogin(LoginView):
    template_name = "blog/login.html"


class MyLogout(LogoutView, LoginRequiredMixin):
    template_name = "blog/logout.html"


def registrarse(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(request, "blog/inicio.html", {"mensaje": f"Usuario: {username_capturado}"})

    else:
        form = UserCreationForm()

    return render(request, "blog/registrarse.html", {"form": form})



@login_required
def editar_perfil(request):
    user = request.user

    if request.method != "POST":
        form = UserEditForm(initial={"email": user.email})
    else: 
        form = UserEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "blog/inicio.html")

    contexto = {"user": user, "form": form}
    return render(request, "blog/editarPerfil.html", contexto)            


@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else: 
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "blog/inicio.html")

    contexto = {"form": form}
    return render(request, "blog/avatar_form.html", contexto)            
