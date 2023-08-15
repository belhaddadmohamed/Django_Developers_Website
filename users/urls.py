from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('profile/<uuid:pk>', views.profile, name="profile"),
]