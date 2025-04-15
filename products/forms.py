from django import forms

from products.models import Category, Reviews


class ProductsFilterForm(forms.Form):

    min_price = forms.IntegerField(required=False, label='Минимальная цена')
    max_price = forms.IntegerField(required=False, label='Максимальная цена')
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Категории'
    )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('text', 'rating')