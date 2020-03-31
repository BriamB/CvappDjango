from django.db import models

# Create your models here.
class Municipio(models.Model):
    municipio= models.CharField(max_length=200)

    def __str__(self):
        return self.municipio

class Departamento(models.Model):
    departamento = models.CharField(max_length=200)
    municipio = models.ForeignKey(Municipio, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.departamento

class Exp_Profesional(models.Model):
    Empresa = models.CharField(max_length=200)
    Departamento = models.ForeignKey(Departamento, null=False, on_delete=models.CASCADE)
    Periodo_inicio = models.DateField()
    Periodo_fin = models.DateField()
    Funciones = models.CharField(max_length=300)

    def __str__(self):
        return self.Empresa

class Formacion(models.Model):
    Centro_educativo = models.CharField(max_length=200)
    Nivel_educativo = models.CharField(max_length=200)
    Estado_estudio = models.CharField(max_length=100)
    Periodo_inicio = models.DateField()
    Periodo_fin = models.DateField()

    def __str__(self):
        return self.Centro_educativo

class Area(models.Model):
    Areas = models.CharField(max_length=50)

    def __str__(self):
        return self.Areas

class Tipo_Identificacion(models.Model):
    Tipo_identificacion = models.CharField(max_length=50)

    def __str__(self):
        return self.Tipo_identificacion

class Cargo(models.Model):
    descripcion = models.CharField(max_length=20)
    def __str__(self):
        return self.descripcion

class cv(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tipo_identificacion = models.ForeignKey(Tipo_Identificacion, null=False, on_delete=models.CASCADE)
    ceduala = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=15)
    estado_civil = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    Departamento = models.ForeignKey(Departamento, null=False, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50)
    licencia = models.CharField(max_length=5)
    foto = models.FileField(null=False, upload_to="Foto/%Y/%m/%d")
    experiencia_profesional = models.ForeignKey(Exp_Profesional, null=False, on_delete=models.CASCADE)
    formacion = models.ForeignKey(Formacion, null=False, on_delete=models.CASCADE)
    idioma = models.CharField(max_length=20)
    nivel = models.CharField(max_length=15)
    estado_laboral = models.CharField(max_length=20)
    area = models.ForeignKey(Area, null=False, on_delete=models.CASCADE)
    salario = models.IntegerField()
    carga_cv = models.FileField(null=False, upload_to="Cv/%Y/%m/%d")
    
