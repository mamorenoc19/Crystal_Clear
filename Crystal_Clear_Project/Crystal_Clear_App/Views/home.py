from django.shortcuts import render, redirect
import random
from django.conf import settings
from django.core.mail import send_mail
from Crystal_Clear_App.models import Estudiante, Clase, Profesor


def home(request):
    return render(request, "Crystal_Clear_App/home/home.html")


def contactar(request):
    if request.method == "POST":
        nombre = request.POST["Name"]
        mensaje = request.POST["Message"] + \
            " / Email: " + request.POST["Email"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["manumorenocordoba@gmail.com"]
        send_mail(nombre, mensaje, email_desde,
                  email_para, fail_silently=False)
        return render(request, "Crystal_Clear_App/home/envio_exitoso.html")
    return render(request, "Crystal_Clear_App/home.html")


def login(request):
    return render(request, "Crystal_Clear_App/home/login.html")


def sign_in(request):
    return render(request, "Crystal_Clear_App/home/sign_in.html")


def home_login(request):
    estudiante = random.choice(lista_estudiante)
    context = {'estudiante': estudiante}
    return render(request, "Crystal_Clear_App/home/home_login.html", context)


lista_estudiante = ['Camila', 'alejandra', 'jose miguel']
