from django.http import HttpResponse
from django.shortcuts import render, redirect
from personas.models import persona
from .forms import PersonaForm

def paginainicio(request):
    return render(request,'PaginaInicio.html')

def Registro(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionusuarios')
    else:
        form = PersonaForm()
    return render(request,'Registro.html',{'form':form})

def gestionusuarios(request):
    no_personas_var = persona.objects.count()
    Personas = persona.objects.all()
    DicMensajes = {'msg1': 'Valor mensaje 1'}
    return render(request,'Gestionusuarios.html', {'no personas':no_personas_var, 'personas':Personas})

def EditarPersona(request, id):
    Persona = persona.objects.get(id = id)
    if request.method == 'GET':
        form = PersonaForm(instance=Persona)
        contexto = {
            'form':form
        }
    else:
        form = PersonaForm(request.POST, instance=Persona)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('gestionusuarios')
    return render(request,'Registro.html', contexto)

def eliminarPersona(request, id):
    Persona = persona.objects.get(id = id)
    Persona.delete()
    return redirect('gestionusuarios')



