from django import forms

from parents.models import Parent
from acount.models import Usuarios


class ParentForm(forms.ModelForm):
     usuario = forms.ModelChoiceField(
        queryset=Usuarios.objects.all(),
        empty_label="Selecione usuario Corespondente",
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Usuario",
    )
     
     class Meta:
        model = Parent                                          
        fields = ["first_name", "last_name", "phone_number", "email", "relationship", "profile_img", "usuario"]
        exclude = [
            "date_created",
            "last_updated",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "relationship": forms.TextInput(attrs={"class": "form-control"}),
            "profile_img": forms.FileInput(attrs={"class": "form-control"}),
        }
