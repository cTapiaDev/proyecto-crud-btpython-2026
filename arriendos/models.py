from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # Nombre, apellidos y correo <- AbstractUser
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255)
    telefono_personal = models.CharField(max_length=15)
    TIPOS = (
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador')
    )
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS, default='arrendatario')


class Inmueble(models.Model):
    arrendador = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo_usuario': 'arrendador'})
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField(default=0)
    habitaciones = models.IntegerField(default=1)
    banos = models.IntegerField(default=1)
    direccion = models.CharField(max_length=255)
    comuna = models.CharField(max_length=100)

    TIPOS_INMUEBLE = (
        ('Casa', 'Casa'),
        ('Departamento', 'Departamento'),
        ('Parcela', 'Parcela')
    )
    tipo_inmueble = models.CharField(max_length=20, choices=TIPOS_INMUEBLE)
    precio_mensual = models.IntegerField()

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    arrendatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitudes_realizadas')
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='solicitudes_recibidas')
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('aceptada', 'Aceptada')], default='pendiente')
    fecha = models.DateTimeField(auto_now_add=True)