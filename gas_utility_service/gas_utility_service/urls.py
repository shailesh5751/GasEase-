from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('accounts/', include('accounts.urls')),
    path('requests/', include('service_requests.urls')),
    path('support/', include('support_dashboard.urls')),
    path('service/', include('service_requests.urls')),
    path('dashboard/', include('support_dashboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
