from django.shortcuts import render, redirect
from .models import Artista
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request,"inicio.html")