from django.urls import path
from . import views

app_name = "cinema"

urlpatterns = [
    path("", views.index, name="index"),
    path("set-preferences/", views.set_preferences, name="set_preferences"),
    path("clear-preferences/", views.clear_preferences, name="clear_preferences"),
]