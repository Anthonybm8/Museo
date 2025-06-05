from django.shortcuts import render, redirect
from .models import Obra
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request,"inicioob.html")