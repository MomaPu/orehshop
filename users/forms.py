from django import forms
from django.contrib.auth import get_user_model



class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()  # Используйте get_user_model()
        fields = ('username', 'email')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'avatar','address')