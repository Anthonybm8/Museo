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
        obra_ids = request.POST.getlist("obra")

        foto = request.FILES.get('foto')
        biografia = request.FILES.get('biografia')

        nuevoArtista = Artista.objects.create(
            nombre=nombre,
            apellido=apellido,
            foto=foto,
            biografia=biografia
        )

        # Evitar IDs vacíos
        for id in obra_ids:
            if id:  # Solo si id no está vacío
                obra = Obra.objects.get(id=id)
                nuevoArtista.obra.add(obra)

        messages.success(request, "Artista guardado exitosamente")
        return redirect('inicio')

def eliminarArtista(request, id):
        artista = Artista.objects.get(id=id)
        artista.delete()
        messages.success(request, "Artista eliminado exitosamente")
        return redirect('inicio')