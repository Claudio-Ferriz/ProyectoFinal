from django.http import HttpResponse
from django.shortcuts import render
from multiprocessing import context
from blog.forms import ArticuloForm, AutorForm, SeccionForm
from blog.models import Articulo, Autor, Seccion

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
        # Hacer algo con la base de datos
        titulo_para_buscar = request.POST["titulo"]
        resultados_de_busqueda = Articulo.objects.filter(titulo=titulo_para_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "blog/resultados-de-la-busqueda.html", context=contexto)

