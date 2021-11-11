from django.shortcuts import render, redirect
import random
from django.conf import settings
from django.core.mail import send_mail
from .models import Estudiante, Clase, Profesor

# Create your views here.
def home(request):
    return render(request, "Crystal_Clear_App/home.html")

def contactar(request):
    if request.method == "POST":
        nombre = request.POST["Name"]
        mensaje = request.POST["Message"] + \
            " / Email: " + request.POST["Email"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["manumorenocordoba@gmail.com"]
        send_mail(nombre, mensaje, email_desde,
                  email_para, fail_silently=False)
        return render(request, "Crystal_Clear_App/envio_exitoso.html")
    return render(request, "Crystal_Clear_App/home.html")

def login(request):
    return render(request, "Crystal_Clear_App/login.html")

def sign_in(request):
    return render(request, "Crystal_Clear_App/sign_in.html")

# ----------------------------------- Home -----------------------------------------


def home_login(request):
    estudiante = random.choice(lista_estudiante)
    context={'estudiante':estudiante}
    return render(request, "Crystal_Clear_App/home_login.html", context)

lista_estudiante = ['Camila', 'alejandra', 'jose miguel']

'''------------------------------- CLASES  --------------------------------------------'''
def clases(request):
    clases = Clase.objects.all()
    context = {'clases': clases}
    return(render(request, "Crystal_Clear_App/clases.html",context))

def clase(request):
    estudiantes = Estudiante.objects.all()
    context = {'estudiante':estudiantes}
    return render(request, "Crystal_Clear_App/clase.html", context)



'''------------------------------- PROFESORES  --------------------------------------------'''

def profesores(request):
    profesores = Profesor.objects.all()
    context = {'profesores': profesores}
    return(render(request, "Crystal_Clear_App/profesores.html", context))




'''------------------------------- ESTUDIANTES  --------------------------------------------'''
def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    context = {'estudiante': estudiantes}
    return render(request, "Crystal_Clear_App/estudiantes.html", context)





'''------------------------------- EXÁMENES  --------------------------------------------'''
def examen(request):
    examenes = Examen.objects.all()
    context = {'examenes': examenes}
    return render(request, "Crystal_Clear_App/examenes.html", context)

def crear_examen(request):
    return render(request, "Crystal_Clear_App/crear_examen.html")

