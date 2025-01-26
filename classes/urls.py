from django.urls import path

from views import classes_views  # Import das views centralizadas

urlpatterns = [
    path("create_class/", classes_views.class_create, name="create_class"),
]

""" path("class_list", classes_views.class_list, name="class_list"),
path("<int:pk>/", classes_views.class_detail, name="class_detail"),
path("<int:pk>/update/", classes_views.class_update, name="class_update"),
path("<int:pk>/delete/", classes_views.class_delete, name="class_delete"), """
