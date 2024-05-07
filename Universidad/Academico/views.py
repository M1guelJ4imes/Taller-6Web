from django.shortcuts import render, redirect
from . models import Persona
from django.contrib import messages

# Create your views here.

def home(request):
    cursos= Persona.objects.all()
    messages.success(request, '¡Cursos Listados!')
    return render(request, "Inclusion.html", {"cursos":cursos})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    materia = request.POST['txtMateria']
    creditos = request.POST['numCreditos']

    curso = Persona.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, materia=materia, creditos=creditos)
    messages.success(request, '¡Curso Registrado!')
    return redirect('/')

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    materia = request.POST['txtMateria']
    creditos = request.POST['numCreditos']

    curso= Persona.objects.get(codigo=codigo)
    curso.nombre=nombre
    curso.apellido=apellido
    curso.materia=materia
    curso.creditos=creditos
    curso.save()
    messages.success(request, '¡Curso Editado!')
    return redirect('/')

def edicionCurso(request,codigo):
    curso= Persona.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso":curso})

def eliminarCurso(request,codigo):
    curso= Persona.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, '¡Curso Eliminado!')
    return redirect('/')