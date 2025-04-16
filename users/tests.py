from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Support
from .forms import UserUpdateForm, CustomUserCreationForm, PasswordResetForm

class UserViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()

    def login_user(self):

        self.client.login(username='testuser', password='testpassword')
	def test_user_profile_get(self):
		self.login_user()
		response = self.client.get(reverse('user_profile'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'users/user_profile.html')
		self.assertIn('form', response.context)

	def test_user_profile_post_valid(self):
		self.login_user()
		data = {
			'username': 'testuser',
			'mail': 'test@mail.ru'
		}
		response = self.client.post(reverse('user_profile'), data)
		self.assertRedirects(response, reverse('user_profile'))

		self.user.refresh_from_db()
		self.assertEqual(self.user.username, 'testuser')

	def test_register_get(self):
		response = self.client.get(reverse('register'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/register.html')
		self.assertIn('form', response.context)

	def test_register_post_valid(self):
		data = {
			'username': 'newuser',
			'password1': 'strongpassword123',
			'password2': 'strongpassword123'
		}
		response = self.client.post(reverse('register'), data)
		self.assertRedirects(response, reverse('home'))
		self.assertTrue(User.objects.filter(username='newuser').exists())

	def test_password_reset_request_get(self):
		response = self.client.get(reverse('password_reset'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/password_reset_form.html')

	def test_password_reset_request_post_valid(self):
		data = {
			'email': self.user.email
		}
		response = self.client.post(reverse('password_reset'), data)
		self.assertRedirects(response, reverse('password_reset_done'))
