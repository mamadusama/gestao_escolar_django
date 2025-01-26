from django import forms

from classes.models import Class
from rooms.models import Room


class ClassForm(forms.ModelForm):
    room = forms.ModelChoiceField(
        queryset=Room.objects.all(),
        empty_label="Selecione uma sala",
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Sala de Aula",
    )

    class Meta:
        model = Class
        fields = ["name", "year", "room", "period"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nome da Turma"}
            ),
            "year": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "2024/2025"}
            ),
            "period": forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            "name": "Nome da Turma",
            "year": "Ano Letivo",
            "room": "Sala de Aula",
            "period": "Período",
        }
