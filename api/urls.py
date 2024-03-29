from django.urls import path
from . import views

# JWT Authorization
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Swagger UI
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="DevSearch API Documentation",
        default_version='v1',
        description="Welcome to the Django Sample Application API documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # User Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Routes
    path('', views.getRoutes, name="route-list-api"),

    # Project
    path('projects/', views.getProjects, name="projects-list-api"),
    path('projects/<uuid:pk>/', views.getProject, name="project-api"),
    path('create-project/', views.ProjectCreateView.as_view(), name="add-project-api"),
    path('update-project/<uuid:pk>/', views.ProjectUpdateView.as_view(), name="update-project-api"),
    path('delete-project/<uuid:pk>/', views.ProjectDeleteView.as_view(), name="delete-project-api"),

    # Tag
    path('tags/', views.getTags, name="tags-list-api"),
    path('create-tag/', views.createTag, name="create-profile-api"),
]