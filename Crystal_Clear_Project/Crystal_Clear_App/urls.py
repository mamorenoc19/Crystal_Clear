from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contacto/", views.contactar, name="contacto"),
    path("login/",views.login, name="login"),
    path("Sign-in/", views.sign_in, name="sign_in"),
    path("home_login/", views.home_login, name='home_login'),
    path("clases/", views.clases, name="clases"),
    path("clase/", views.clase, name='clase'),
    path("profesores/", views.profesores, name="profesores"),
    path("crear_profesores/", views.crear_profesor, name='crear_profesores'),
    path("estudiantes/", views.estudiantes, name="estudiantes"),
    path("crear_estudiantes/", views.crear_estudiantes, name='crear_estudiantes'),
    path("examen/", views.examen, name="examen"),
    path("crear_clase/", views.crear_clase, name='crear_clase'),
    path("crear_login/", views.crear_examen, name='crear_examen'),
]
