from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django import forms
from Crystal_Clear_App.models import Estudiante

class estudiante_form(forms.ModelForm):
    
    class Meta:

        model = Estudiante

        fields = [
            'nombre',
            'apellido',
            'edad',
            'correo',
            'contraseña',
            'sexo',
        ]

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'correo': 'Correo',
            'contraseña': 'Contraseña',
            'sexo': 'Sexo',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
        }



def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    context = {'estudiante': estudiantes}
    return render(request, "Crystal_Clear_App/estudiante/estudiantes.html", context)


def crear_estudiantes(request):
    if request.method == 'POST':
        form = estudiante_form(request.POST)
        if form.is_valid():
            form.save()
            form = estudiante_form()
        return redirect('estudiantes')
    else:
        form = estudiante_form()
    return render(request, "Crystal_Clear_App/estudiante/crear_estudiantes.html", {'form': form})
