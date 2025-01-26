from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

"""    class CargoChoices(models.TextChoices):
        ADMIN = "admin", "Administrador"
        ESTUDANTE = "estudante", "Estudante"
        PROFESSOR = "professor", "Professor"
        FUNCIONARIO = "funcionario", "Funcionário"
        RESPONSAVEL = "responsavel", "Responsável"
 """
from .managers import UsuariosManager

CARGO_CHOICES = (
    (1, "Administrador"),
    (2, "Diretor"),
    (3, "Sub Diretor"),
    (4, "Financeiro"),
    (5, "Atendimento"),
    (6, "Estudante"),
    (7, "Professor"),
    (8, "Responsável"),
)


class Usuarios(AbstractBaseUser, PermissionsMixin):

    nome_usuario = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Nome de Usuário",
    )
    email = models.EmailField(unique=True, blank=False, null=False, max_length=255)

    cargo = models.IntegerField(
        null=False,
        blank=False,
        choices=CARGO_CHOICES,
        verbose_name="Cargo",
    )

    is_staff = models.BooleanField(default=False, verbose_name="É staff?")
    is_active = models.BooleanField(default=True, verbose_name="Está ativo?")
    date_joined = models.DateTimeField(
        default=timezone.now, verbose_name="Data de cadastro"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    # Evitar a criação de last_name
    last_name = None
    first_name = None
    objects = UsuariosManager()
    # Configuração do campo de login e campos obrigatórios
    USERNAME_FIELD = "nome_usuario"
    REQUIRED_FIELDS = ["email", "password"]

    def __str__(self):
        return self.nome_usuario
