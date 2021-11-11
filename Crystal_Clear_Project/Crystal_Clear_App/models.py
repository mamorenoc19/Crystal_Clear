from django.db import models

# Create your models here.


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.SmallIntegerField(default=0)
    correo = models.EmailField(max_length=254)
    contraseña = models.CharField(max_length=50)
    sexos = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=sexos, default='M')

    def nombreCompleto(self):
        cadena = '{0}, {1}'
        return cadena.format(self.nombre, self.apellido)

    def __str__(self):
        return self.nombreCompleto()


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.SmallIntegerField(default=0)
    correo = models.EmailField(max_length=254)
    contraseña = models.CharField(max_length=50)
    sexos = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=sexos, default='M')

    def nombreCompleto(self):
        cadena = '{0}, {1}'
        return cadena.format(self.nombre, self.apellido)

    def __str__(self):
        return self.nombreCompleto()


class Clase(models.Model):
    nombre = models.CharField(max_length=50, default='', blank=True)
    descripcion = models.CharField(max_length=250)
    creditos = models.PositiveSmallIntegerField()
    profesor = models.ForeignKey(Profesor, null=False, blank=False, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    estudiantes = models.ManyToManyField(Estudiante, blank=True)
    lista_estudiantes = []
    num_estudiantes = 0

    def nombreCurso(self):
        cadena = '{0}, Créditos: {1}'
        return cadena.format(self.nombre, self.creditos)

    def __str__(self):
        return self.nombreCurso()


class Pregunta(models.Model):
    pregunta = models.CharField(max_length=250)
    tipo_pregunta = ((1, 'Escrita'), (2, "Verdadero_Falso"),
                     (3, "Opcion_multiple"))
    opciones_respuesta = ((1, 'Vedadero'), (0, 'Falso'))
    opcion_respuesta = models.CharField(
        choices=opciones_respuesta, max_length=1, default=1)
    respuesta_correcta = models.BooleanField()

class PreguntaVedaderoFalso(models.Model):
    marks=models.PositiveIntegerField()
    pregunta=models.CharField(max_length=600)
    opcion1=models.CharField(max_length=200)
    opcion2=models.CharField(max_length=200)
    opcion3=models.CharField(max_length=200)
    opcion4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Estadistica(models.Model):
    puntaje = models.SmallIntegerField()


class Examen(models.Model):
    clase = models.ForeignKey(Clase, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, default='', blank=True)
    num_preguntas = models.PositiveIntegerField()
    estado = models.BooleanField(default=True)



class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    descripcion = models.CharField(max_length=250)
