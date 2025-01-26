import re

from django.db import models
from django.forms import ValidationError

from rooms.models import Room


def validate_year_format(value):
    if not re.match(r"^\d{4}/\d{4}$", value):
        raise ValidationError("O formato do ano letivo deve ser 'AAAA/AAAA'.")


class PeriodChoices(models.TextChoices):
    MORNING = "morning", "Manhã"
    AFTERNOON = "afternoon", "Tarde"
    EVENING = "evening", "Noite"


class Class(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da Turma")
    year = models.CharField(
        max_length=9,
        validators=[
            validate_year_format,
        ],
        verbose_name="Ano Letivo",
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Sala de Aula",
        related_name="classes",
    )

    period = models.CharField(
        max_length=10,
        choices=PeriodChoices.choices,
        verbose_name="Período",
    )

    student_count = models.PositiveIntegerField(
        default=0, verbose_name="Quantidade de Alunos"
    )

    def __str__(self):
        return f"{self.name} - {self.year}"


""" 
    def can_add_student(self):
        """
# Verifica se a turma pode receber mais alunos, com base na capacidade da sala.
"""
        if self.room and self.student_count >= self.room.capacity:
            return False
        return True 
"""
