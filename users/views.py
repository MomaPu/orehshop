from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.forms import UserUpdateForm, CustomUserCreationForm, PasswordResetForm
from django.contrib import messages

from users.models import Support


@login_required
def user_profile(request):
	user = request.user

	if request.method == 'POST':
		form = UserUpdateForm(request.POST, request.FILES, instance=request.user)  # Используем новую форму
		if form.is_valid():
			form.save()
			return redirect('user_profile')
	else:
		form = UserUpdateForm(instance=request.user)  # Используем новую форму

	return render(request, 'users/user_profile.html', {
		'user': user,
		'form': form,
	})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт для {username} успешно создан! Теперь вы можете войти.')
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            pass
            return redirect("password_reset_done")
    else:
        form = PasswordResetForm()
    return render(request=request, template_name="registration/password_reset_form.html", context={"password_reset_form":form})

def support_view(request):
	if request.method == 'POST':
		mail = request.POST.get('recipient-name')
		text = request.POST.get('message-text')

		Support.objects.create(mail=mail, text=text)

	return render(request, 'users/support.html')