from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import home, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    
    
    path('users/', include('apps.users.urls')),
    path('moderator/', include('apps.moderator.urls')),
    path('storage/', include('apps.storage.urls')),
    path('refectory/', include('apps.refectory.urls')),
    path('loans/', include('apps.loans.urls')),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)