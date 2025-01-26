from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50, verbose_name="Sala")
    capacity = models.PositiveIntegerField(verbose_name="Capacidade")
    location = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Localização da Sala"
    )

    def __str__(self):
        return f"{self.name} (Capacidade: {self.capacity})"
