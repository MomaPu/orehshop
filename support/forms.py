from django import forms


class SupportForm(forms.Form):
    reciept_name = forms.EmailField(label='Email', max_length=254)
    message_text = forms.CharField(label='Сообщение',widget=forms.Textarea)
    