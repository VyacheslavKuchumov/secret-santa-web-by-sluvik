"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.views.generic.base import RedirectView

urlpatterns = [
    # Redirect root to admin
    path('', RedirectView.as_view(url='/admin/', permanent=True)),

    # Admin panel
    path('admin/', admin.site.urls),

    # Auth / accounts app
    path('api/accounts/', include('accounts.urls')),

    # Secret Santa app (replace 'secret_santa' with your actual app folder name)
    path('api/secret-santa/', include('secret_santa.urls')),

    # Django Debug Toolbar
    path('__debug__/', include(debug_toolbar.urls)),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
