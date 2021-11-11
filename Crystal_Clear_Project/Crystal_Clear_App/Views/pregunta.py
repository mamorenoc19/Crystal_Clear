from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django import forms
from Crystal_Clear_App.models import Estudiante, Clase, Examen, Profesor,Pregunta, PreguntaVedaderoFalso


class pregunta_form(forms.ModelForm):

    class Meta:
        model = PreguntaVedaderoFalso
        fields = [
            'pregunta',
            'opcion1',
            'opcion2',
            'opcion3',
            'opcion4',
            'answer',
            'marks',
        ]
        labels = {
            'pregunta':'Pregunta',
        }

        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }


def pregunta(request):
    preguntas = Pregunta.objects.all()
    context = {'preguntas': preguntas}
    return(render(request, "Crystal_Clear_App/examen/examen_2.html", context))


def editar_examen(request):
    if request.method == 'POST':
        form = pregunta_form(request.POST)
        if form.is_valid():
            form.save()
            form = pregunta_form()
        return redirect('examen')
    else:
        form = pregunta_form()
    return render(request, "Crystal_Clear_App/examen/examen.html", {'form': form})
