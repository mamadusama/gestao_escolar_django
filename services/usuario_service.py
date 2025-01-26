from django.contrib.auth import get_user_model

User = get_user_model()


def register_user(user_entity):
    """
    Serviço para criar um novo usuário baseado em uma UserEntity.
    """
    user = User.objects.create_user(
        nome_usuario=user_entity.nome_usuario,
        email=user_entity.email,
        password=user_entity.password,
        cargo = user_entity.cargo,
    )
    user.is_staff = user_entity.is_staff
    user.is_active = user_entity.is_active
    user.cargo = user_entity.cargo
    user.save()
    return user
