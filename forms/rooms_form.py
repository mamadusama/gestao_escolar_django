from django import forms

from rooms.models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["name", "location", "capacity"]

        """    widgets = {
            "year": forms.TextInput(attrs={"placeholder": "Ex: 2024/2025"}),
            "student_count": forms.NumberInput(attrs={"min": 0}),
        } """
        """ labels = {
            "name": "Nome da Turma",
            "year": "Ano Letivo",
            "period": "Período",
        } """
