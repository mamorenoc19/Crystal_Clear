from django.shortcuts import render, redirect
import random
from django.conf import settings
from django.core.mail import send_mail
from django import forms
from Crystal_Clear_App.models import Estudiante, Clase

class clase_form(forms.ModelForm):

    class Meta:

        model = Clase

        fields = [
            'nombre',
            'descripcion',
            'creditos',
            'profesor',
        ]

        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'creditos': 'Creditos',
            'profesor': 'Profesor',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'creditos': forms.NumberInput(attrs={'class': 'form-control'}),
            'profesor': forms.Select(attrs={'class': 'form-control'}),
        }

def clases(request):
    clases = Clase.objects.all()
    context = {'clases': clases}
    return(render(request, "Crystal_Clear_App/clases/clases.html",context))


def clase(request):
    estudiantes = Estudiante.objects.all()
    context = {'estudiante':estudiantes}
    return render(request, "Crystal_Clear_App/clases/clase.html", context)


def crear_clase(request):
    if request.method == 'POST':
        form = clase_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('clases')
    else:
        form = clase_form()
    return render(request, "Crystal_Clear_App/clases/crear_clase.html", {'form': form})

