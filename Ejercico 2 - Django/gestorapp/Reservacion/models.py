from django.db import models
from Vuelo.models import Vuelo

class Pasajero(models.Model):
    nombre = models.CharField(max_length = 255);
    direccion = models.CharField(max_length = 255);
    telefono = models.CharField(max_length = 255);

    def __str__(self) -> str:
        return f'Pasajero {self.id}: {self.nombre}';

class Reservacion(models.Model):
    vuelo = models.ForeignKey(Vuelo, on_delete=models.SET_NULL, null = True);
    pasajero = models.ForeignKey(Pasajero, on_delete=models.SET_NULL, null = True);
    aciento = models.CharField(max_length = 255);

    def __str__(self) -> str:
        return f'Reservacion {self.id}: Vuelo {self.vuelo} de {self.pasajero}';
