from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from miapp.forms import FormArticulo
from django.contrib import messages


# Create your views here.

def cursos(request):

    return render(request , 'cursos.html')

def crear_cursos(request):
    return render(request, 'crear_cursos.html')

def carreras(request) :    
        return render(request, 'carreras.html')

def rango2(request,a=0,b=100) :


    return HttpResponse(layout)

def crear_articulo(request,titulo, contenido, publicado):
    articulo = Articulo(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")

def buscar_articulo(request):
    try:
        articulo = Articulo.objects.get(id=1000)
        resultado = f"""Articulo: 
                        <br> <strong>ID:</strong> {articulo.id} 
                        <br> <strong>Título:</strong> {articulo.titulo} 
                        <br> <strong>Contenido:</strong> {articulo.contenido}
                        """
    except:
        resultado = "<h1> Artículo No Encontrado </h1>"
    return HttpResponse(resultado)

def editar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)
    articulo.titulo = "Enseñanza onLine en la UNTELS"
    articulo.contenido = "Aula Virtual, Google Meet, Portal Académico, Google Classroom..."
    articulo.publicado = False

    articulo.save()
    return HttpResponse(f"Articulo Editado: {articulo.titulo} - {articulo.contenido}")

def listar_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'listar_articulos.html',{
           'articulos':articulos,
            'titulo': 'Listado de Artículos'
    })

    
def eliminar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)
    articulo.delete()
    return redirect('listar_articulos')

def save_articulo(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        if len(titulo)<=5:
            return HttpResponse("<h2>El tamaño del título es pequeño, intente nuevamente</h2>")
        contenido = request.POST['contenido']
        publicado = request.POST['publicado']
 
        articulo = Articulo(
            titulo = titulo,
            contenido = contenido,
            publicado = publicado
        )
        articulo.save()
        # Crear un mensaje flash (Sesión que solo se muestra 1 vez)
        messages.success(request, f'Se agregó correctamente el artículo {articulo.id}')
        return redirect('listar_articulos')
    else:
        return HttpResponse("<h2>No se ha podido registrar el artículo</h2>")

def crear_carreras(request):
    return render(request, 'crear_carreras.html')

def create_full_articulo(request):
    if request.method == 'POST':
        formulario = FormArticulo(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            # Hay 2 formas de recuperar la información
            titulo  = data_form.get('titulo')
            contenido = data_form['contenido']
            publicado = data_form['publicado']
            articulo = Articulo(
                titulo = titulo,
                contenido = contenido,
                publicado = publicado
            )
            articulo.save()
            # Crear un mensaje flash (Sesión que solo se muestra 1 vez)
            messages.success(request, f'Se agregó correctamente el artículo {articulo.id}')
            return redirect('listar_articulos')
            #return HttpResponse(articulo.titulo + ' -  ' + articulo.contenido + ' - ' + str(articulo.publicado))

    else:
        formulario = FormArticulo()
        # Generamos un formulario vacío

    return render(request, 'create_full_articulo.html',{
        'form': formulario
    })




