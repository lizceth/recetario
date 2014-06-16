from recetario.models import Receta, Comentario
from recetario.forms import RecetaForm, ComentarioForm, ContactoForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def inicio(request):
    recetas = Receta.objects.all()
    total = recetas.count()
    return render(request, 'recetario/inicio.html',
                  {'recetas':recetas, 'total':total})

def usuarios(request):
    usuarios = User.objects.all()
    recetas = Receta.objects.all()
    return render(request, 'recetario/usuarios.html',
                  {'usuarios':usuarios, 'recetas':recetas})

def sobre(request):
    titulo='sobre'
    return render_to_response('recetario/sobre.html', {'titulo':titulo},context_instance=RequestContext(request))

def contacto(request):
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde el recetario de Maestros del Web'
            contenido = formulario.cleaned_data['mensaje'] + "\n"
            contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['abel.huanca@upeu.pe'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    return render_to_response('recetario/contactoform.html',{'formulario':formulario}, context_instance=RequestContext(request))



def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetario/recetas.html', {'recetas':recetas})

def detalle_receta(request, id_receta):
    receta = get_object_or_404(Receta, id=id_receta)
    comentarios = Comentario.objects.filter(receta=receta)
    return render(request, 'recetario/receta.html',
                  {'receta':receta, 'comentarios':comentarios})

def nueva_receta(request):
    if request.method=='POST':
        formulario = RecetaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas')
    else:
        formulario = RecetaForm()
    return render_to_response('recetario/recetaform.html',
                              {'formulario':formulario},
                              context_instance=RequestContext(request))

def nuevo_comentario(request):
    if request.method=='POST':
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas')
    else:
        formulario = ComentarioForm()
    return render_to_response('recetario/comentarioform.html',
                              {'formulario': formulario},
                              context_instance=RequestContext(request))

def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('recetario/nuevousuario.html',
                              {'formulario': formulario},
                              context_instance=RequestContext(request))

def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render_to_response('recetario/noactivo.html',
                                              context_instance=RequestContext(request))
            else:
                return render_to_response('recetario/nousuario.html',
                                          context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('recetario/ingresar.html', {'formulario': formulario},
                              context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    return render_to_response('recetario/privado.html', {'usuario': usuario},
                              context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')


