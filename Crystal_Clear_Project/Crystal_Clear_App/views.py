from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, "Crystal_Clear_App/home.html")

def login(request):
    return render(request, "Crystal_Clear_App/login.html")

def sign_in(request):
    return render(request, "Crystal_Clear_App/sign_in.html")

def home_login(request):
    estudiante = random.choice(lista_estudiante)
    context={'estudiante':estudiante}
    return render(request, "Crystal_Clear_App/home_login.html", context)

lista_estudiante = ['Camila', 'alejandra', 'jose miguel']

def clases(request):
    return(render(request, "Crystal_Clear_App/clases.html"))

def clase(request):
    context = {'estudiante':estudiante}
    return render(request, "Crystal_Clear_App/clase.html", context)


estudiante = [{'nombre': 'camila', 'numero': 1},
                    {'nombre': 'jose', 'numero': 2}, {'nombre': 'milerna', 'numero': 3}, {'nombre': 'carlos', 'numero': 4}]

def examen(request):
    return render(request, "Crystal_Clear_App/examen.html")

def crear_clase(request):
    return render(request, "Crystal_Clear_App/crear_clase.html")



def crear_examen(request):
    return render(request, "Crystal_Clear_App/crear_examen.html")

