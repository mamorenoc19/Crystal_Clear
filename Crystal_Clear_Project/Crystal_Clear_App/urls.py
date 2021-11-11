from django.urls import path
from . import views
from Crystal_Clear_App.Views.home import home, contactar, sign_in, login, home_login
from Crystal_Clear_App.Views.clases import clases, crear_clase, clase
from Crystal_Clear_App.Views.estudiante import estudiantes, crear_estudiantes
from Crystal_Clear_App.Views.profesor import profesores, crear_profesor
from Crystal_Clear_App.Views.examen import examenes, crear_examen
from Crystal_Clear_App.Views.pregunta import editar_examen, pregunta

urlpatterns = [
    path("", home, name="home"),
    path("contacto/", contactar, name="contacto"),
    path("login/",login, name="login"),
    path("Sign-in/", sign_in, name="sign_in"),
    path("home_login/", home_login, name='home_login'),
    path("clases/", clases, name="clases"),
    path("clase/", clase, name='clase'),
    path("crear_clase/", crear_clase, name='crear_clase'),
    path("profesores/", profesores, name="profesores"),
    path("crear_profesores/", crear_profesor, name='crear_profesores'),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("crear_estudiantes/", crear_estudiantes, name='crear_estudiantes'),
    path("examenes/", examenes, name="examenes"),
    path("examen/", (editar_examen, pregunta), name="examen"),
    path("crear_examen/", crear_examen, name='crear_examen'),
]
