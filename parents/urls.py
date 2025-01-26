from django.urls import path

from views import parents_views  # Import das views centralizadas

urlpatterns = [
    path("create_parent/",parents_views.create_parent,name="create_parent"),

    path("parent_list/",parents_views.parent_list,name="parent_list"),
]
