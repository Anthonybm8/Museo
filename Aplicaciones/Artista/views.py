from django.shortcuts import render, redirect
from .models import Artista
from Aplicaciones.Obra.models import Obra
from django.contrib import messages

# Create your views here.
def inicio(request):
    listadoArtistas = Artista.objects.all()
    return render(request,"inicio.html", {'artistas': listadoArtistas})

def nuevoArtista(request):
    robras = Obra.objects.all()
    return render(request, "nuevoArtista.html", {'obras': robras})

def guardarArtista(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        obra_ids = request.POST.getlist("Obra")

        foto = request.FILES.get('foto')
        biografia = request.FILES.get('biografia')

        nuevoArtista = Artista.objects.create(
            nombre=nombre,
            apellido=apellido,
            foto=foto,
            biografia=biografia

        )
        messages.success(request, "Artista guardado exitosamente")
        return redirect('inicio')