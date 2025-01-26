from django.contrib import admin

from rooms.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "capacity")
    list_filter = ("name",)
