from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import create_review

urlpatterns = [
	path('product/<int:product_id>/review/', create_review, name='create_review'),
	]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)