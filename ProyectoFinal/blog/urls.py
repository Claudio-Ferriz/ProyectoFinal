from django.contrib import admin
from django.urls import path, include

from blog.views import (
    buscar,
    mostrar_inicio,
    procesar_formulario_autor,
    procesar_formulario_articulo,
    procesar_formulario_seccion,
    AutorList,
    AutorDetalle,
    AutorCreate,
    AutorUpdateView,
    AutorDelete,
    MyLogin,
    MyLogout,
    registrarse,
    editar_perfil,
    agregar_avatar,
    
    )


urlpatterns = [
    path("inicio/", mostrar_inicio),
    path("formulario-autor/", procesar_formulario_autor),
    path("formulario-articulo/", procesar_formulario_articulo),
    path("formulario-seccion/", procesar_formulario_seccion),
    path("formulario-de-busqueda/", buscar),
    path("autor/list", AutorList.as_view(), name= "List"),
    path("r'(?P<pk>\d+)^$'", AutorDetalle.as_view(), name= "Detail"),
    path("r'nuevo^$'", AutorCreate.as_view(), name= "New"),
    path("r'editar/(?P<pk>\d+)^$'", AutorUpdateView.as_view(), name= "Edit"),
    path("r'borrar/(?P<pk>\d+)^$'", AutorDelete.as_view(), name= "Delete"),
    path("login/", MyLogin.as_view(), name="login"),
    path("logout/", MyLogout.as_view(), name="logout"),
    path("registrarse/", registrarse, name="registrarse"),
    path("editar-perfil/", editar_perfil, name= "EditarPerfil"),
    path("agregar-avatar/", agregar_avatar, name="AgregarAvatar"),
]
