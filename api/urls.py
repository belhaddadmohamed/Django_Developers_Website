from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


urlpatterns += [
    path('', views.getRoutes, name="list"),
    path('projects/', views.getProjects, name="projects-list"),
    path('projects/<uuid:pk>/', views.getProject, name="project"),
    path('create-project/', views.createProject, name="add-project"),

    path('tags/', views.getTags, name="tags-list"),
    path('create-tag/', views.createTag, name="create-profile"),
]