from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal
from .models import Products

class ProductsViewsTest(TestCase):

    def setUp(self):
        # Создаём тестового клиента
        self.client = Client()
        # Создаём тестовые продукты
        self.product1 = Products.objects.create(name='TestProduct1', price=Decimal('15.99'))
        self.product2 = Products.objects.create(name='TestProduct2', price=Decimal('25.50'))

    def test_products_list_view(self):
        response = self.client.get(reverse('main_page.html'))  # предполагаем, что есть такой URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/main_page.html')  # предполагаемый шаблон
        self.assertContains(response, self.product1.name)
        self.assertContains(response, self.product2.name)

    def test_product_detail_view(self):
        response = self.client.get(reverse('product_tile', args=[self.product1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_title.html')
        self.assertContains(response, self.product1.name)
        self.assertContains(response, str(self.product1.price))



