from django.shortcuts import render, redirect
from django import forms
from django.conf import settings
from django.core.mail import send_mail
from Crystal_Clear_App.models import Estudiante, Clase, Examen, Profesor, PreguntaVedaderoFalso

class examen_form(forms.ModelForm):
    
    class Meta:

        model = Examen

        fields = [
            'clase',
            'nombre',
            'num_preguntas',
        ]

        labels = {
            'clase': 'Clase del examen',
            'nombre': 'Nombre',
            'num_preguntas': 'Número de preguntas',
        }

        widgets = {
            'clase': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'num_preguntas': forms.NumberInput(attrs={'class': 'form-control'}),
        }
def examenes(request):
    examenes = Examen.objects.all()
    context = {'examenes': examenes}
    return render(request, "Crystal_Clear_App/examen/examenes.html", context)


def crear_examen(request):
    if request.method == 'POST':
        form = examen_form(request.POST)
        if form.is_valid():
            form.save()
            form = examen_form()
        return redirect('examenes')
    else:
        form = examen_form()
    return render(request, "Crystal_Clear_App/examen/crear_examen.html", {'form': form})

