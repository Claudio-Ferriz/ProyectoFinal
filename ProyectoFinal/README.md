# ProyectoFinal
Los creadores de este proyecto son Claudio Ferriz y Conrado Perez.

Somos estudiantes de programación en Coderhouse, actualmente haciendo el curso de Python, en este creamos un blog mediante el uso del framework de Django.

Durante el proyecto fuimos dividiendo las tareas pero ayudandonos mutuamente todo el tiempo mediante meets y liveshare de VisualStudioCode.

División de trabajo: Nos separamos algunas cosas especificas para hacer cada uno(no quiere decir que no sepamos hacerlas por nuestra cuenta), la primera entrega del proyecto final fue la base para terminar el proyecto, la hicimos en conjunto también.

Claudio Ferriz: -CRUD
                -Avatar
                -Modificación de usuario
                
Conrado Perez:  -Tests
                -Login,Logout, Registrarse
                -Formulario Autor, Formulario Sección, Formulario Artículo, Formulario de Busqueda
                
URLS:

1.http://127.0.0.1:8000/blog/formulario-articulo/ --> Te lleva al formulario para un nuevo articulo.         
2.http://127.0.0.1:8000/blog/formulario-seccion/ --> Te lleva al formulario para una nueva sección.       
3.http://127.0.0.1:8000/blog/formulario-autor/ --> Te lleva al formulario para un nuevo autor.        
4.http://127.0.0.1:8000/blog/formulario-de-busqueda/ --> busca un articulo que quieras y lo muestra.       
5.http://127.0.0.1:8000/blog/autor/list --> lista de todos los autores                          
6.http://127.0.0.1:8000/blog/r'(?P<pk>\d+)^$' --> detalle de cada autor                      
7.http://127.0.0.1:8000/blog/r'editar/(?P<pk>\d+)^$' --> permite editar un autor                           
8.http://127.0.0.1:8000/blog/r'borrar/ --> permite borrar un autor                              
9.http://127.0.0.1:8000/blog/r'nuevo^$' --> permite crear un autor nuevo                            
10.http://127.0.0.1:8000/blog/login/ --> permite logearse en el sitio web                           
11.http://127.0.0.1:8000/blog/logout/ --> permite deslogearse del sitio web                          
12.http://127.0.0.1:8000/blog/registrarse/ --> permite registrarse en el sitio web                         
13.http://127.0.0.1:8000/blog/editar-perfil/ --> permite editar un perfil previamente creado                  
14.http://127.0.0.1:8000/blog/agregar-avatar/ --> permite agregar un avatar                        

