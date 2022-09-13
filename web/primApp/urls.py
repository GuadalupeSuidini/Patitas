
from xml.dom.minidom import Document
from django.urls import path
from .views import contacto, datos_mascota, eliminardatos, fichaUsuario, ing_usuarios, inicio, ingreso_usuarios, lista_mascotas, registro, lista_usuario, editarusuario
from django.urls import path, include
from .views import ( datos_mascota, editarFicha, 
eliminardatos, inicio, ingreso_usuarios, lista_mascotas, registro, lista_usuario, editarusuario, ficha
, eliminarFicha, acercaDeMi, buscar_mas, amigos)
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', lista_mascotas, name = 'inicio'), #LISTO


############ url ingreso usuarios
    path('Login',ingreso_usuarios, name = 'login'),
    path('Registar',registro, name = 'registrar'),
    path('Usuarios',ing_usuarios, name = 'usuarios'),
    path('Misdatos',lista_usuario, name = 'misdatos'),
    path('logout/',LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('edita-datos/<id>/',editarusuario, name = 'ediusuarios'),
    path('elimina-datos/<id>/',eliminardatos, name = 'eliminardatos'),
############################################################


     path('acercaDeMi', acercaDeMi , name = 'acercaDeMi'),
     path('contacto', contacto , name = 'contacto'),
     path('amigos', amigos, name='amigos'),
     path('fichaUsuario/<int:id>', fichaUsuario, name='fichaUsuario'),

##########################################################
     path('listamascotas',lista_mascotas, name = 'mismascotas'),
     path('Mascotas', datos_mascota, name = 'mascotas'), #LISTO
     path('editarFicha/<int:id>',editarFicha, name = 'editarFicha'),
     path('ficha/<int:id>',ficha,name="ficha"),
     path('eliminarFicha/<int:id>',eliminarFicha,name="eliminarFicha"),
     path('buscar/',buscar_mas, name="Buscar"),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)