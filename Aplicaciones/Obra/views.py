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

def editarObra(request, id):
    obra = Obra.objects.get(id=id)
    return render(request, "editarObra.html", {'obra': obra})

def procesarEdicionObra(request, id):
    obra = Obra.objects.get(id=id)
    
    if request.method == 'POST':
        # Procesar el formulario
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha_creacion_str = request.POST.get('fecha_creacion')  # Obtenemos como string
        foto = request.FILES.get('foto')
        informacion = request.FILES.get('informacion')
        
        # Validar que la fecha no esté vacía
        if not fecha_creacion_str:
            messages.error(request, "La fecha de creación es obligatoria")
            return render(request, "editarObra.html", {'obra': obra})
        
        try:
            # Convertir string a objeto date
            from datetime import datetime
            fecha_creacion = datetime.strptime(fecha_creacion_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Formato de fecha inválido. Use YYYY-MM-DD")
            return render(request, "editarObra.html", {'obra': obra})
        
        obra.titulo = titulo
        obra.descripcion = descripcion
        obra.fecha_creacion = fecha_creacion
        
        if foto:
            obra.foto = foto
        if informacion:
            obra.informacion = informacion
            
        try:
            obra.save()
            messages.success(request, "Obra editada exitosamente")
            return redirect('inicioob')
        except Exception as e:
            messages.error(request, f"Error al guardar: {str(e)}")
            return render(request, "editarObra.html", {'obra': obra})
    
    # Si es GET, mostrar el formulario
    return render(request, "editarObra.html", {'obra': obra})