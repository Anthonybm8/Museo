from django.urls import path
from . import views
urlpatterns=[
    path('inicioob',views.inicio,name='inicioob'),
]