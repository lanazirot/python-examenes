from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length = 255);

    def __str__(self) -> str:
        return f'Ciudad {self.id}: {self.nombre}';

class Vuelo(models.Model):
    nombre = models.CharField(max_length = 255);
    descripcion = models.CharField(max_length = 500);
    ciudadOrigen = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null = True, related_name='ciudadOrigen_content_type');
    ciudadDestino = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null = True, related_name='ciudadDestino_content_type');
    fecha = models.DateField();

    def __str__(self) -> str:
        return f'Vuelo {self.id}: {self.nombre}';