from django.urls import path
from . import views
urlpatterns=[
    path('inicioob',views.inicio,name='inicioob'),
    path('nuevaObra',views.nuevaObra,name='nuevaObra'),
    path('guardarObra',views.guardarObra,name='guardarObra'),
    path('eliminarObra/<id>',views.eliminarObra,name='eliminarObra'),
    path('editarObra/<id>',views.editarObra,name='editarObra'),
    path('procesarEdicionObra/<id>',views.procesarEdicionObra,name='procesarEdicionObra'),
]