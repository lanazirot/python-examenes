from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length = 255);
    puesto = models.CharField(max_length = 255);
    correoElectronico = models.CharField(max_length = 255);

    def __str__(self) -> str:
        return f'Usuario {self.id}: {self.nombre}';
