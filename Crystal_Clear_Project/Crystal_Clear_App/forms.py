from django import forms
from Crystal_Clear_App.models import Clase


class claseForm(forms.ModelForm):

    class Meta:

        model = Clase

        fields = [
            'nombre',
            'descripcion',
            'creditos',
            'profesor',
            'estado',
        ]

        labels = {
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'creditos':'Creditos',
            'profesor':'Profesor',
            'estado':'Estado',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'creditos': forms.NumberInput(attrs={'class': 'form-control'}),
            'profesor': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
