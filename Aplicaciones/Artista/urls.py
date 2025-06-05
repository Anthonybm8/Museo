from django.urls import path
from . import views
urlpatterns=[
    path('inicio',views.inicio,name='inicio'),
    path('nuevoArtista',views.nuevoArtista,name='nuevoArtista'),
    path('guardarArtista',views.guardarArtista,name='guardarArtista'),
    path('eliminarArtista/<id>', views.eliminarArtista, name='eliminarArtista'),
    path('editarArtista/<id>', views.editarArtista, name='editarArtista'),
    path('procesarEdicionArtista/<id>', views.procesarEdicionArtista, name='procesarEdicionArtista'),
]