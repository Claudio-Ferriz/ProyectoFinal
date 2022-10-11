from django.http import HttpResponse
from django.shortcuts import render
from multiprocessing import context
from blog.forms import ArticuloForm, AutorForm, SeccionForm
from blog.models import Articulo

# Create your views here.


def mostrar_inicio(request):
    return HttpResponse("Bienvenidos al inicio")

def procesar_formulario_autor(request):
    contexto = {}
    return render(request,"blog/formulario-autor.html", context=contexto)

def procesar_formulario_articulo(request):
    contexto = {}
    return render(request,"blog/formulario-articulo.html",context=contexto)

def procesar_formulario_seccion(request):
    contexto = {}
    return render(request,"blog/formulario-seccion.html",context=contexto)

def buscar(request):
    if  request.method == "GET":
        return render(request, "blog/formulario-de-busqueda.html")

    if request.method == "POST":
        # Hacer algo con la base de datos
        titulo_para_buscar = request.POST["titulo"]
        resultados_de_busqueda = Articulo.objects.filter(titulo=titulo_para_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "blog/resultados-de-la-busqueda.html", context=contexto)
