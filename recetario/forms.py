# coding:utf-8
from django.forms import ModelForm
from django import forms
from recetario.models import Receta, Comentario

class RecetaForm(ModelForm):
    class Meta:
        model = Receta

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario


