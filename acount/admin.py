from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from acount.models import Usuarios
from forms.user_forms import UsuarioChangeForm, UsuarioCreationForm
from parents.models import Parent
from students.models import Student


class CustomUserAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuarios
    ordering = ("nome_usuario",)
    list_display = ("nome_usuario", "email", "cargo", "is_active", "is_staff")
    fieldsets = (
        (None, {"fields": ("nome_usuario", "email", "password", "cargo")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("nome_usuario", "email", "password1", "password2", "cargo"),
            },
        ),
    )





class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "student_number",
        "email",
        "parent",
        "is_active",
    )
    search_fields = ("first_name", "last_name", "student_number", "email")
    list_filter = ("gender", "nationality", "is_active")
    readonly_fields = ("student_number", "date_created", "last_updated")

    fieldsets = (
        (None, {"fields": ("user", "parent", "is_active")}),
        (
            "Informações Pessoais",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "date_of_birth",
                    "gender",
                    "nationality",
                )
            },
        ),
        ("Contato", {"fields": ("phone_number", "email")}),
        ("Endereço", {"fields": ("address", "city", "neighborhood", "postal_code")}),
        ("Adicional", {"fields": ("profile_img", "student_number")}),
        ("Auditoria", {"fields": ("date_created", "last_updated")}),
    )


admin.site.register(Student, StudentAdmin)
admin.site.register(Usuarios, CustomUserAdmin)
