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
    path("examen/", views.examen, name="examen"),
    path("crear_clase/", views.crear_clase, name='crear_clase'),
    path("crear_login/", views.crear_examen, name='crear_examen'),
]
