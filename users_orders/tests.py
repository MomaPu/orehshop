from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from decimal import Decimal
from .models import Products, Order

class CartAndOrderViewsTest(TestCase):

    def setUp(self):
        # Создаём тестового пользователя и авторизуемся
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

        # Создаём тестовые продукты
        self.product1 = Products.objects.create(name='Product 1', price=Decimal('10.50'))
        self.product2 = Products.objects.create(name='Product 2', price=Decimal('20.00'))

    def test_add_to_cart(self):
        # Добавляем продукт и проверяем содержимое сессии
        response = self.client.get(reverse('add_to_cart', args=[self.product1.id]))
        self.assertRedirects(response, reverse('home'))
        session_cart = self.client.session.get('cart', {})
        self.assertEqual(session_cart[str(self.product1.id)], 1)

        # Добавляем тот же продукт ещё раз
        response = self.client.get(reverse('add_to_cart', args=[self.product1.id]))
        session_cart = self.client.session.get('cart', {})
        self.assertEqual(session_cart[str(self.product1.id)], 2)

        # Добавляем другой продукт
        response = self.client.get(reverse('add_to_cart', args=[self.product2.id]))
        session_cart = self.client.session.get('cart', {})
        self.assertEqual(session_cart[str(self.product2.id)], 1)

    def test_cart_view(self):
        # Устанавливаем корзину вручную
        session = self.client.session
        session['cart'] = {
            str(self.product1.id): 2,
            str(self.product2.id): 3
        }
        session.save()

        response = self.client.get(reverse('cart_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product 1')
        self.assertContains(response, 'Product 2')
        self.assertIn('cart_items', response.context)
        self.assertIn('total_price', response.context)
        total_price = response.context['total_price']
        self.assertEqual(total_price, self.product1.price * 2 + self.product2.price * 3)

    def test_create_order_with_items(self):
        # Установка корзины
        session = self.client.session
        session['cart'] = {
            str(self.product1.id): 1,
            str(self.product2.id): 2
        }
        session.save()

        response = self.client.post(reverse('create_order'))
        self.assertRedirects(response, reverse('user_profile'))
        # Проверка, что заказ создан
        order = Order.objects.filter(user=self.user).first()
        self.assertIsNotNone(order)
        self.assertEqual(order.total_price, float(self.product1.price + self.product2.price * 2))
        # Корзина очищена
        self.assertEqual(self.client.session.get('cart'), {})

    def test_create_order_empty_cart(self):
        # Пустая корзина
        self.client.session['cart'] = {}
        self.client.session.save()
        response = self.client.get(reverse('create_order'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Корзина пуста')

    def test_user_orders(self):
        # Создаём заказ заранее
        Order.objects.create(user=self.user, total_price=30.0, products=[])
        response = self.client.get(reverse('user_orders'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'users_orders.html')
        self.assertIn('orders', response.context)
        self.assertEqual(len(response.context['orders']), 1)