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


class Pregunta(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    preguntas = ((1, 'Escrita'), (2, "Verdadero_Falso"),
                 (3, "Opcion_multiple"))
    pregunta = models.CharField(choices=preguntas, max_length=1, default=1)
    respuesta = models.BooleanField()


class Estadistica(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    puntaje = models.SmallIntegerField()


class Examen(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    preguntas = models.ManyToManyField(Pregunta)
    estadisticas = models.ForeignKey(Estadistica, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    num_preguntas = models.PositiveIntegerField()
    estado = models.BooleanField(default=True)


class Clase(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    creditos = models.PositiveSmallIntegerField()
    profesor = models.ForeignKey(Profesor, null=False, blank=False, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    estudiantes = models.ManyToManyField(Estudiante, blank=True)
    examenes = models.ManyToManyField(Examen, blank=True)
    lista_estudiantes = []
    num_estudiantes = 0

    def nombreCurso(self):
        cadena = '{0}, Créditos: {1}'
        return cadena.format(self.nombre, self.creditos)

    def __str__(self):
        return self.nombreCurso()
    
    # def __str__(self):
    #     self.lista_estudiantes = []
    #     num_estudiantes = self.int(input('Cuantos estudiantes tendrá su clase?:'))
    #     for i in range(num_estudiantes):
    #         self.lista_estudiantes.append(estudiantes[i])
    #     return self.lista_estudiantes
    

    #  def __str__(self):
    #      num_estudiantes = self.int(input('Cuantos estudiantes hay en la clase?: '))
    #     while num_estudiantes > len(lista_estudiantes):
    #         self.lista_estudiantes.append(estudiantes)


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    descripcion = models.CharField(max_length=250)
