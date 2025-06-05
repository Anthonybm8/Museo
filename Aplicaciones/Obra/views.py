from django.shortcuts import render, redirect
from .models import Obra
from django.contrib import messages

# Create your views here.
def inicio(request):
    listadoObras = Obra.objects.all()
    return render(request,"inicioob.html", {'obras': listadoObras})

def nuevaObra(request):
    return render(request, "nuevaObra.html")

def guardarObra(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha_creacion = request.POST.get('fecha_creacion')
        foto = request.FILES.get('foto')
        informacion = request.FILES.get('informacion')

        nuevaObra = Obra.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            fecha_creacion=fecha_creacion,
            foto=foto,
            informacion=informacion
        )
        messages.success(request,"Cargo guardado exitosamente")
        return redirect('inicioob')    

def eliminarObra(request, id):
    obraEliminar = Obra.objects.get(id=id)
    obraEliminar.delete()
    messages.success(request, "Obra eliminada exitosamente")
    return redirect('inicioob')