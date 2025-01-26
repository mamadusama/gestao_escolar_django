from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UsuariosManager(BaseUserManager):
    """
    Gerenciador para o modelo de usuário customizado.
    """

    def create_user(self, nome_usuario, email, cargo, password, **extra_fields):
        """
        Cria e retorna um usuário normal.
        """
        if not nome_usuario:
            raise ValueError("O campo nome_usuario é obrigatório.")
        if not email:
            raise ValueError("O campo email é obrigatório.")
        if not cargo:
            raise ValueError("O campo cargo é obrigatório.")

        # Normaliza o email
        email = self.normalize_email(email)

        # Define os valores padrão adicionais
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", False)

        # Cria e retorna o usuário
        user = self.model(
            nome_usuario=nome_usuario, email=email, cargo=cargo, **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nome_usuario, email, password, **extra_fields):
        """
        Cria e retorna um superusuário.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # Garantir que os valores necessários estejam definidos
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superusuário precisa ter is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superusuário precisa ter is_superuser=True.")

        # Usa o método create_user para criar o superusuário
        return self.create_user(
            nome_usuario=nome_usuario,
            email=email,
            cargo=1,
            password=password,
            **extra_fields
        )
