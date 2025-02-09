from django.urls import path
from .views import *



app_name = "teams"

urlpatterns = [
    path("", teams, name="teams"),
]