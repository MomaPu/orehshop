from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home, product_detail, shop_info

urlpatterns = [
	path('', home, name='home'),
	path('products/<int:id>/', product_detail, name='product_detail'),
	path('info', shop_info, name='info'),
	]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
