from django.contrib import admin
from parents.models import Parent
from forms.parents_form import ParentForm


class ParentAdmin(admin.ModelAdmin):
    form = ParentForm  # Define o formulário personalizado para o admin
    list_display = ("first_name", "last_name", "email", "phone_number", "relationship","profile_img")
    search_fields = ("first_name", "last_name", "email", "phone_number")
    list_filter = ("relationship",)
    ordering = ("first_name",)

    fieldsets = (
        (None, {
            "fields": ("usuario", "first_name", "last_name", "phone_number", "email", "relationship", "profile_img")
        }),
        ("Informações Adicionais", {
            "fields": ("date_created", "last_updated"),
            "classes": ("collapse",),  # Colapsa essas informações no admin
        }),
    )

    readonly_fields = ("date_created", "last_updated")  # Torna os campos somente leitura


# Registra o modelo no admin
admin.site.register(Parent, ParentAdmin)
