from django.db import models

from parents.models import Parent
from acount.models import Usuarios



# Escolhas de Gênero
class GenderChoices(models.TextChoices):
    MASCULINO = "M", "Masculino"
    FEMININO = "F", "Feminino"
    OUTRO = "O", "Outro"


# Nacionalidades
class NationalityChoices(models.TextChoices):
    BRASILEIRO = "BR", "Brasileiro"
    PORTUGUES = "PT", "Português"
    GUINEENSE = "GB", "Guineense"
    SENEGALENSE = "SN", "Senegalense"
    OUTRO = "OT", "Outro"


class Student(models.Model):
    # Relacionamento com o modelo de usuário
    usuario = models.OneToOneField(
        Usuarios,
        on_delete=models.CASCADE,
        related_name="student",
        verbose_name="Usuário",
    )

    # Relacionamento com os pais ou responsável
    parent = models.ForeignKey(
        Parent,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name="Responsável",
    )

    # Informações Pessoais
    first_name = models.CharField(max_length=150, verbose_name="Nome")
    last_name = models.CharField(max_length=150, verbose_name="Sobrenome")
    date_of_birth = models.DateField(verbose_name="Data de Nascimento")
    gender = models.CharField(
        max_length=1, choices=GenderChoices.choices, verbose_name="Gênero"
    )
    nationality = models.CharField(
        max_length=2,
        choices=NationalityChoices.choices,
        default=NationalityChoices.OUTRO,
        verbose_name="Nacionalidade",
    )

    # Contato
    phone_number = models.CharField(max_length=15, verbose_name="Telefone")
    email = models.EmailField(max_length=260, verbose_name="Email")

    # Endereço
    address = models.TextField(verbose_name="Endereço")
    city = models.CharField(max_length=100, verbose_name="Cidade")
    neighborhood = models.CharField(max_length=100, verbose_name="Bairro")
    postal_code = models.CharField(max_length=10, verbose_name="Código Postal")

    # Informações Adicionais
    student_number = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        verbose_name="Número do Aluno",
    )
    profile_img = models.ImageField(
        null=True, blank=True, upload_to="student_profile_images", verbose_name="Foto de Perfil"
    )
    is_active = models.BooleanField(default=True, verbose_name="Ativo")

    # Auditoria
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Criação"
    )
    last_updated = models.DateTimeField(
        auto_now=True, verbose_name="Última Atualização"
    )

    def __str__(self):
        return f"{self.first_name} Nº - {self.student_number}"
