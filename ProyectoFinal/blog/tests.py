from django.test import TestCase
from blog.models import Autor


class ViewTestCase(TestCase):

    def test_crear_autor(self):
        Autor.objects.create(nombre="Agustin", apellido="Ratatouille", profesion="astronauta")
        todos_los_autores = Autor.objects.all()
        assert len(todos_los_autores) == 1
        assert todos_los_autores[0].nombre == "Agustin"


#   def test_crear_autor_sin_profesion(self):
 #       Autor.objects.create(nombre="Lautaro",profesion="pastelero")
   #     todos_los_autores = Autor.objects.all()
  #      assert todos_los_autores[0].profesion is None


#   def test_crear_5_autores():
 #       Autor.objects.create(nombre="Agustin", apellido="Sarabia", profesion="maestro")
  #      Autor.objects.create(nombre="Sofia", apellido="Perez",profesion="ingeniero")
   #     Autor.objects.create(nombre="Ernesto", apellido="Goldenberg",profesion="florero")
    #    Autor.objects.create(nombre="Aaron", apellido="Molina",profesion="musico")
     #   Autor.objects.create(nombre="Fernando", apellido="Godoy",profesion="geologo")
     #   todos_los_autores = Autor.objects.all()
      #  assert len(todos_los_autores) == 15
        
