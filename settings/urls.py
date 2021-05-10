from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('journal/', include('admin_dashboard.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.accounts.urls')),
    path('api/journal/', include('journal.urls')),
    path('api/user/', include('users.urls')),
    path('api-docs/', include('settings.api_docs')),

    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
