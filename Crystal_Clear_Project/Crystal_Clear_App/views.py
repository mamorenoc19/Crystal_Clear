from django.shortcuts import render
import random
from django.conf import settings
from django.core.mail import send_mail
from Crystal_Clear_App.forms import claseForm
from .models import Estudiante, Clase

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

def clases(request):
    clases = Clase.objects.all()
    context = {'clases': clases}
    return(render(request, "Crystal_Clear_App/clases.html",context))

def clase(request):
    estudiantes = Estudiante.objects.all()
    context = {'estudiante':estudiantes}
    return render(request, "Crystal_Clear_App/clase.html", context)


#estudiante = [{'nombre': 'camila', 'numero': 1},
 #                   {'nombre': 'jose', 'numero': 2}, {'nombre': 'milerna', 'numero': 3}, {'nombre': 'carlos', 'numero': 4}]

def examen(request):
    return render(request, "Crystal_Clear_App/examen.html")

def crear_clase(request):
    if request.method == 'POST':
        form = claseForm(request.POST)
        if form.is_valid():
            form.save()
        # return redirect('Managemet_Inventory_App:inventory')
    else:
        form = claseForm()
    return render(request, "Crystal_Clear_App/crear_clase.html",{'form':form})



def crear_examen(request):
    return render(request, "Crystal_Clear_App/crear_examen.html")

