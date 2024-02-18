from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("projects/", include('projects.urls')),
    path("", include('users.urls')),
    path("api/", include('api.urls')),
        
    # Reset Password:
    # 1- User submits email for reset  (PasswordResetView)
    # 2- Email sent message  (PasswordResetDoneView)
    # 3- Email with link and reset instructions  (PasswordResetConfirmView)
    # 4- Password successfully reset message  (PasswordResetCompleteView)

    path("reset_password/", auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

