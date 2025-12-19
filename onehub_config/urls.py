"""
Main URL configuration for OneHub project.
Handles routing for dashboard and API endpoints.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),
    
    # Dashboard URLs
    path('dashboard/', include('dashboard.urls')),
    
    # API endpoints
    path('api/v1/', include('api.urls')),
    
    # Health check
    path('health/', include('health_check.urls')),
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
