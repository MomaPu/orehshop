from django import forms

from products.models import Category


class ProductsFilterForm(forms.Form):

    min_price = forms.IntegerField(required=False, label='Минимальная цена')
    max_price = forms.IntegerField(required=False, label='Максимальная цена')
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Категории'
    )

