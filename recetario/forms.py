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

class ContactoForm(forms.Form):
    correo = forms.EmailField(label='Tu correo Electrónico')
    mensaje = forms.CharField(widget=forms.Textarea)
