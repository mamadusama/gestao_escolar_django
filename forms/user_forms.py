from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from acount.models import Usuarios


class UsuarioCreationForm(forms.ModelForm):
    """Formulário para criação de novos usuários, com validação de senha."""

    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmação de Senha", widget=forms.PasswordInput
    )

    class Meta:
        model = Usuarios
        fields = ["nome_usuario", "email", "cargo"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não correspondem.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])  # Define a senha do usuário
        if commit:
            user.save()
        return user


class UsuarioChangeForm(forms.ModelForm):
    """Formulário para edição de usuários existentes no admin."""

    password = ReadOnlyPasswordHashField(
        label="Senha",
        help_text=(
            "As senhas não são armazenadas em texto plano, então não é possível visualizar a senha. "
            'Você pode redefinir a senha usando <a href="../password/">este formulário</a>.'
        ),
    )

    class Meta:
        model = Usuarios
        fields = ["nome_usuario", "email", "cargo", "is_active", "is_staff"]
