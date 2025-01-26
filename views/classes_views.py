from django.shortcuts import get_object_or_404, redirect, render

from classes.models import Class
from entities import classes
from forms.classes_forms import ClassForm
from services import class_service


# Criar Turma
def class_create(request):
    if request.method == "POST":
        classes_form = ClassForm(request.POST)
        if classes_form.is_valid():
            name = classes_form.cleaned_data["name"]
            year = classes_form.cleaned_data["year"]
            room = classes_form.cleaned_data["room"]
            period = classes_form.cleaned_data["period"]
            # student_count = classes_form.cleaned_data["student_count"]

            new_class = classes.ClassEntity(
                name=name,
                year=year,
                room=room,
                period=period,
                # student_count=student_count,
            )

            class_service.register_classes(new_class)

            return redirect("class_list")
    else:
        classes_form = ClassForm()
    return render(request, "classes/class_form.html", {"classes_form": classes_form})


""" # Listar todas as Turmas
def class_list(request):
    classes = Class.objects.all()
    return render(request, "classes/classes_list.html", {"classes": classes})


# Detalhar uma Turma
def class_detail(request, pk):
    turma = get_object_or_404(Class, pk=pk)
    return render(request, "classes/classes_detail.html", {"class": turma})


# Editar uma Turma existente
def class_update(request, pk):
    turma = get_object_or_404(Class, pk=pk)
    if request.method == "POST":
        classes_form = ClassForm(request.POST, instance=turma)
        if classes_form.is_valid():
            classes_form.save()
            return redirect("class_list")
    else:
        classes_form = ClassForm(instance=turma)
    return render(request, "classes/classes_form.html", {"classes_form": classes_form})


# Deletar uma Turma
def class_delete(request, pk):
    turma = get_object_or_404(Class, pk=pk)
    if request.method == "POST":
        turma.delete()
        return redirect("class_list")
    return render(request, "classes/classes_confirm_delete.html", {"class": turma})
 """
