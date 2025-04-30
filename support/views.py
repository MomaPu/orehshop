from django.shortcuts import render, redirect
from .forms import SupportForm
from .services import create_support_request
def support_view(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['recipient_name']
            text = form.cleaned_data['message_text']

            create_support_request(mail, text)

            return redirect('support_success')

        return render(request, 'users/support.html', {'form': form})

    form = SupportForm()
    return render(request, 'users/support.html', {'form': form})