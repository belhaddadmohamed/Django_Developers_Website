from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerUser, name="register"),

    path('', views.profiles, name="profiles"),
    path('profile/<uuid:pk>', views.userProfile, name="user-profile"),
    path('account/', views.userAccount, name="user-account"),
    path('edit-account/', views.editAccount, name="edit-account"),
    
    path('create-skill/', views.create_skill, name="create-skill"),
    path('update-skill/<uuid:pk>/', views.update_skill, name="update-skill"),
    path('delete-skill/<uuid:pk>/', views.delete_skill, name="delete-skill"),

    path('inbox/', views.inbox, name="inbox"),
    path('message/<uuid:pk>/', views.viewMessage, name="message"),
    path('create-message/<uuid:pk>/', views.createMessage, name="create-message"),
]