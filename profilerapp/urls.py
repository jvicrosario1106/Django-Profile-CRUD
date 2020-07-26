from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("users/", views.users, name="users"),
    path("add/", views.add, name="add"),
    path("addprocess/", views.addprocess, name="addprocess"),
    path("details/<str:pk>/", views.details, name="details"),
    path("delete/<str:pk>/", views.delete, name="delete"),
    path("update/<str:pk>/", views.update, name="update"),
    path("updateprocess/<str:pk>/", views.updateprocess, name="updateprocess"),

] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)