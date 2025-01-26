from django import forms

from acount.models import Usuarios
from parents.models import Parent
from students.models import Student


class StudentForm(forms.ModelForm):
    """
    Formulário para o modelo Student.
    """

    usuario = forms.ModelChoiceField(
        queryset=Usuarios.objects.all(),
        empty_label="Selecione usuario Corespondente",
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Usuario",
    )
    parent = forms.ModelChoiceField(
        queryset=Parent.objects.all(),
        empty_label="Selecione usuario Encaregado do Aluno",
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Encaregado",
    )

    class Meta:
        model = Student
        exclude = [
            "student_number",
            "is_active",
        ]  # O usuário será tratado separadamente no formulário UserForm.

        fields = ["first_name", "last_name", "phone_number", "email", "gender", "profile_img", "usuario", "date_of_birth", "nationality", "address", "city", "neighborhood", "postal_code", "parent"]

        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "Primeiro Nome", "class": "form-control"}
            ),
            "last_name": forms.TextInput(
                attrs={"placeholder": "Último Nome", "class": "form-control"}
            ),
            "date_of_birth": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "nationality": forms.Select(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(
                attrs={"placeholder": "Telefone", "class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "E-mail", "class": "form-control"}
            ),
            "address": forms.Textarea(
                attrs={"placeholder": "Endereço", "class": "form-control", "rows": 3}
            ),
            "city": forms.TextInput(
                attrs={"placeholder": "Cidade", "class": "form-control"}
            ),
            "neighborhood": forms.TextInput(
                attrs={"placeholder": "Bairro", "class": "form-control"}
            ),
            "postal_code": forms.TextInput(
                attrs={"placeholder": "Código Postal", "class": "form-control"}
            ),
            "profile_img": forms.FileInput(attrs={"class": "form-control"}),
        }
