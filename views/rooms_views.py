from django.shortcuts import get_object_or_404, redirect, render

from entities import room
from forms.rooms_form import RoomForm
from services import rooms_service


# Criar Sala
def room_create(request):
    if request.method == "POST":
        rooms_form = RoomForm(request.POST)
        if rooms_form.is_valid():
            name = rooms_form.cleaned_data["name"]
            location = rooms_form.cleaned_data["location"]
            capacity = rooms_form.cleaned_data["capacity"]

            new_room = room.RoomEntity(name=name, location=location, capacity=capacity)

            rooms_service.register_rooms(new_room)

            # classes_form.save()
            return redirect("rooms_list")
    else:
        rooms_form = RoomForm()
    return render(request, "rooms/rooms_form.html", {"rooms_form": rooms_form})


# Listar todas as turmas
""" def class_list(request):
    classes = Class.objects.all()
    return render(request, "classes/class_list.html", {"classes": classes})


# Detalhar uma turma
def class_detail(request, pk):
    turma = get_object_or_404(Class, pk=pk)
    return render(request, "classes/class_detail.html", {"class": turma})


# Editar uma turma existente
def class_update(request, pk):
    turma = get_object_or_404(Class, pk=pk)
    if request.method == "POST":
        form = ClassForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            return redirect("class_list")
    else:
        form = ClassForm(instance=turma)
    return render(request, "classes/class_form.html", {"form": form})


# Deletar uma turma
def class_delete(request, pk):
    turma = get_object_or_404(Class, pk=pk)
    if request.method == "POST":
        turma.delete()
        return redirect("class_list")
    return render(request, "classes/class_confirm_delete.html", {"class": turma})
 """
