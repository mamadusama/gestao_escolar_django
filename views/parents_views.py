from django.shortcuts import redirect, render

from entities import parents
from forms.parents_form import ParentForm
from services import parent_service 


def create_parent(request):
    if request.method == "POST":
        parent_form = ParentForm(request.POST, request.FILES)
        if parent_form.is_valid():
            # Dados do formulário
            first_name = parent_form.cleaned_data["first_name"]
            last_name = parent_form.cleaned_data["last_name"]
            phone_number = parent_form.cleaned_data["phone_number"]
            email = parent_form.cleaned_data["email"]
            relationship = parent_form.cleaned_data["relationship"]
            profile_img = parent_form.cleaned_data["profile_img"]
            usuario = parent_form.cleaned_data["usuario"]  # O usuário selecionado

            # Criação da entidade de pai
            new_parent = parents.ParentEntity(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                email=email,
                relationship=relationship,
                profile_img=profile_img,
                usuario=usuario,  # Passando o usuário selecionado
            )

            # Registrar o pai (salvar no banco de dados)
            parent_service.register_parent(new_parent)

            return redirect("parent_list")
    else:
        parent_form = ParentForm()

    return render(
        request,
        "parents/parent_form.html",
        {"parent_form": parent_form},
    )


def parent_list(request):
    parents = parent_service.list_parents()
    return render(request, "parents/list_parents.html", {"parents": parents})