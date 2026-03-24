from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import settings



def health(request):
    return HttpResponse("OK")

urlpatterns = [
    path('health/', health),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('assets/img/favicon.png'))),
    path('admin/', admin.site.urls),
    path('', include('bunkering_frontend.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
