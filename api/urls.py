from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name="list"),
    path('projects/', views.getProjects, name="projects-list"),
    path('projects/<uuid:pk>/', views.getProject, name="project"),
    path('create-project/', views.createProject, name="add-project"),

    path('profiles/', views.getProfiles, name="profiles-list"),
    path('profiles/<uuid:pk>/', views.getProfile, name="profile"),
    path('create-profile/', views.createProfile, name="create-profile"),

    path('tags/', views.getTags, name="tags-list"),
    path('create-tag/', views.createTag, name="create-profile"),
]