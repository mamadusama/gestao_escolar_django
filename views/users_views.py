from django.shortcuts import redirect, render

from entities.usuario import UserEntity
from forms.user_forms import UsuarioCreationForm
from services.usuario_service import register_user


def create_user(request):
    if request.method == "POST":
        user_form = UsuarioCreationForm(request.POST)
        if user_form.is_valid():
            nome_usuario = user_form.cleaned_data["nome_usuario"]
            email = user_form.cleaned_data["email"]
            password = user_form.cleaned_data["password1"]
            cargo = user_form.cleaned_data["cargo"]

            user_entity = UserEntity(
                nome_usuario=nome_usuario,
                email=email,
                password=password,
                cargo=cargo,
            )
            register_user(user_entity)
            return redirect("user_list")
    else:
        user_form = UsuarioCreationForm()

    return render(request, "acount/user_form.html", {"user_form": user_form})
