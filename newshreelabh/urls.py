from django.urls import path
from newshreelabh import views

urlpatterns = [
    path("", views.home, name="home"),
]