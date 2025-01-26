from django.urls import path

from views import rooms_views  # Import das views centralizadas

urlpatterns = [
    path("create_room/", rooms_views.room_create, name="create_room"),
]

""" path("class_list", rooms_views.class_list, name="class_list"),
    path("<int:pk>/", rooms_views.class_detail, name="class_detail"),
    path("<int:pk>/update/", rooms_views.class_update, name="class_update"),
    path("<int:pk>/delete/", rooms_views.class_delete, name="class_delete"), 
"""
