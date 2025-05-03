from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import ReviewForm
from products.models import Products
from .services import create_product_review

@login_required
def create_review(request, product_id):

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                review = create_product_review(product_id, request.user, form.cleaned_data)
                return redirect(reverse('product_detail', kwargs={'id_product': product_id}))
            except ValueError as e:
                product = Products.objects.get(pk=product_id)
                context = {
                    'product': product,
                    'form': form,
                    'error_message': str(e),
                }
                return render(request, 'product_title.html', context)

        else:
            product = Products.objects.get(pk=product_id)
            context = {
                'product': product,
                'form': form,
            }
            return render(request, 'product_title.html', context)
    else:
        product = Products.objects.get(pk=product_id)
        form = ReviewForm()
        context = {
            'product': product,
            'form': form,
        }
        return render(request, 'product_title.html', context)