from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import get_homepage, get_product_detail

urlpatterns = [
	path('', get_homepage, name='home'),
	path('product/<int:id_product>/', get_product_detail, name='product_detail'),
	]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)