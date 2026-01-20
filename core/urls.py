from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import home, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    #path('almoxarifado/', almoxarifado, name='almoxarifado'),
    
    
    path('accounts/', include('accounts.urls')),
    path('moderator/', include('moderator.urls')),
    path('almoxarifado/', include('almoxarifado.urls')),
    path('almocar/', include('almocar.urls'))
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)