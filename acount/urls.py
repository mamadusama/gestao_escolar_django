from django.urls import path

from views import users_views  # Import das views centralizadas

urlpatterns = [
    path("create_user/", users_views.create_user, name="create_user"),
]
