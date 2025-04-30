from django.urls import path
from .views import support_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('support/', support_view, name='support_view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)