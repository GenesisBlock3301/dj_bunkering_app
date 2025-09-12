from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.http import HttpResponse
from . import settings



def health(request):
    return HttpResponse("OK")

urlpatterns = [
    path('health/', health),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('bunkering_frontend.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
