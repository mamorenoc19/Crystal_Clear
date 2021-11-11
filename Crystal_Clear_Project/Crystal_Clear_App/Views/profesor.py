from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django import forms
from Crystal_Clear_App.models import Profesor


class profesor_form(forms.ModelForm):

    class Meta:

        model = Profesor

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

def profesores(request):
    profesores = Profesor.objects.all()
    context = {'profesores': profesores}
    return(render(request, "Crystal_Clear_App/profesor/profesores.html", context))


def crear_profesor(request):
    if request.method == 'POST':
        form = profesor_form(request.POST)
        if form.is_valid():
            form.save()
            form = profesor_form()
        return redirect('profesores')
    else:
        form = profesor_form()
    return render(request, "Crystal_Clear_App/profesor/crear_profesores.html", {'form': form})
