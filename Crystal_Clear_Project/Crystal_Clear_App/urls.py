from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/",views.login, name="login"),
    path("Sign-in/", views.sign_in, name="sign_in"),
    path("home_login/", views.home_login, name='home_login'),
    path("clase/", views.clase, name='clase'),
    path("crear_clase/", views.crear_clase, name='crear_clase'),
    path("crear_login/", views.crear_examen, name='crear_examen'),
]
