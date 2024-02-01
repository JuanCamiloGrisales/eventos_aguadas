from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    '''Model definition for Evento.'''
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    desde = models.TimeField(null=True, blank=True)
    hasta = models.TimeField(null=True, blank=True)
    todo_el_dia = models.BooleanField(default=False)
    organizador = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organizador")
    lugar = models.CharField(max_length=100)
    cupos = models.IntegerField(default=0, null=True, blank=True)
    cupos_maximos = models.IntegerField(null=True, blank=True)
    cupos_ilimitados = models.BooleanField(default=False)
    precio = models.CharField(max_length=100, null=True, blank=True, default="Gratuito")
    imagen = models.ImageField(upload_to="eventos_aguadas/", null=True, blank=True)
    adicional = models.TextField(null=True, blank=True)
    asistentes = models.ManyToManyField(User, related_name="asistentes", blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        '''Meta definition for Evento.'''

        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.titulo