from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import shop_info

urlpatterns = [

	path('info', shop_info, name='info'),

	]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)