from products.models import Products


class ProductFilter:
    def __init__(self, max_price=None, min_price=None, with_reviews_only=False):
        self.max_price = max_price
        self.min_price = min_price
        self.with_reviews_only = with_reviews_only
    def find(self):
        qs = Products.objects.all()

        if self.min_price is not None:
            qs = qs.filter(price__gte=self.min_price)

        if self.max_price is not None:
            qs = qs.filter(price__lte=self.max_price)

        if self.with_reviews_only:
            qs = qs.filter(Отзыв__isnull=False).distinct()
        return qs

def get_products():

    return Products.objects.all()