from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home, product_detail, shop_info, create_review

urlpatterns = [
	path('', home, name='home'),
	path('product/<int:id_product>/', product_detail, name='product_detail'),
	path('info', shop_info, name='info'),
	path('product/<int:product_id>/review/', create_review, name='create_review'),
	]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)