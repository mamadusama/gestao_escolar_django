from django.contrib import admin

from classes.models import Class

# Register your models here.


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "student_count", "period")
    list_filter = ("year", "period")
