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

def editarArtista(request, id):
    artista = Artista.objects.get(id=id)
    obras = Obra.objects.all()  # Obtener todas las obras disponibles
    return render(request, "editarArtista.html", {
        'artista': artista,
        'obras': obras  # Pasar las obras al template
    })

def procesarEdicionArtista(request, id):
    artista = Artista.objects.get(id=id)
    
    if request.method == 'POST':
        # Procesar el formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        obra_ids = request.POST.getlist("obra")

        foto = request.FILES.get('foto')
        biografia = request.FILES.get('biografia')

        # Actualizar los campos del artista
        artista.nombre = nombre
        artista.apellido = apellido
        artista.foto = foto if foto else artista.foto  # Mantener la foto actual si no se sube una nueva
        artista.biografia = biografia if biografia else artista.biografia  # Mantener la biografía actual

        artista.save()

        # Actualizar las obras asociadas
        artista.obra.clear()  # Limpiar las obras actuales
        for id in obra_ids:
            if id:  # Solo si id no está vacío
                obra = Obra.objects.get(id=id)
                artista.obra.add(obra)

        messages.success(request, "Artista editado exitosamente")
        return redirect('inicio')