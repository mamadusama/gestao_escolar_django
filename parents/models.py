from django.db import models

from acount.models import Usuarios


class Parent(models.Model):
    usuario = models.OneToOneField(Usuarios, on_delete=models.CASCADE, related_name="usuario")
    first_name = models.CharField(max_length=150, verbose_name="Primeiro Nome")
    last_name = models.CharField(max_length=150, verbose_name="Último Nome")
    phone_number = models.CharField(max_length=15, verbose_name="Número de Telefone")
    email = models.EmailField(verbose_name="E-mail", unique=True)
    relationship = models.CharField(
        max_length=50,
        verbose_name="Relacionamento com o Estudante",
        null=True,
        blank=True,
    )
    profile_img = models.ImageField(upload_to="parent_profiles", null=True, blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Criação"
    )
    last_updated = models.DateTimeField(
        auto_now=True, verbose_name="Última Atualização"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
