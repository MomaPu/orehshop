from django.urls import path, include
from users.views import register, user_profile
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('register/', register, name='register'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('accounts/logout/', LogoutView.as_view(next_page='get_news'), name='logout'),
	path('profile/', user_profile, name='user_profile'),
	path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration//password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration//password_reset_confirm.html'), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration//password_reset_complete.html'), name='password_reset_complete'),
	path('accounts/logout/', LogoutView.as_view(next_page='get_news'), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
