# Generated by Django 5.1.5 on 2025-01-25 01:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Usuarios",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "nome_usuario",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Nome de Usuário"
                    ),
                ),
                ("email", models.EmailField(max_length=255, unique=True)),
                (
                    "cargo",
                    models.IntegerField(
                        choices=[
                            (1, "Administrador"),
                            (2, "Diretor"),
                            (3, "Sub Diretor"),
                            (4, "Financeiro"),
                            (5, "Atendimento"),
                            (6, "Estudante"),
                            (7, "Professor"),
                            (8, "Responsável"),
                        ],
                        verbose_name="Cargo",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="É staff?"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Está ativo?"),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Data de cadastro",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Atualizado em"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
