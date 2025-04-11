from django import forms

class ProductsFilterForm(forms.Form):

    min_price = forms.IntegerField(required=False, label='Минимальная цена')
    max_price = forms.IntegerField(required=False, label='Максимальная цена')

