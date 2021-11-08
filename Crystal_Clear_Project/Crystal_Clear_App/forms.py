from django import forms
from Crystal_Clear_App.models import Clase, Profesor, Estudiante


class claseForm(forms.ModelForm):

    class Meta:

        model = Clase

        fields = [
            'nombre',
            'descripcion',
            'creditos',
            'profesor',
        ]

        labels = {
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'creditos':'Creditos',
            'profesor':'Profesor',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'creditos': forms.NumberInput(attrs={'class': 'form-control'}),
            'profesor': forms.Select(attrs={'class': 'form-control'}),
        }
#PROFESOR
class profesorForm(forms.ModelForm):
    
    class Meta:

        model = Profesor

        fields = [
            'nombre',
            'apellido',
            'edad',
            'correo',
            'contraseña',
            'sexo',
        ]

        labels = {
            'nombre':'Nombre',
            'apellido':'Apellido',
            'edad':'Edad',
            'correo':'Correo',
            'contraseña':'Contraseña',
            'sexo':'Sexo',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
        }
#ESTUDIANTE


class estudianteForm(forms.ModelForm):

    class Meta:

        model = Estudiante

        fields = [
            'nombre',
            'apellido',
            'edad',
            'correo',
            'contraseña',
            'sexo',
        ]

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'correo': 'Correo',
            'contraseña': 'Contraseña',
            'sexo': 'Sexo',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
        }
