from products.models import Products


CATEGORY_CHOICES = {
    '1': 'Миндаль',
    '2': 'Макадами',
    '3': 'Кедровые',
    '4': 'Фисташки',
    '5': 'Бразильские',
    '6': 'Пекан',
    '7': 'Кедровые',
    '8': 'Кешью',
    '9': 'Кедровые',
    '10': 'Фундук',
    '11': 'Грецкий орех',
    '12': 'Арахис',
}


class CourseFilter:
    def __init__(self, max_price=None, min_price=None, category=None):
        self.max_price = max_price
        self.min_price = min_price
        self.category = category
    def find(self):
        qs = Products.objects.all()

        if self.min_price is not None:
            qs = qs.filter(price__gte=self.min_price)

        if self.max_price is not None:
            qs = qs.filter(price__lte=self.max_price)

        if self.category:
            qs = qs.filter(category_id=self.category)

        return qs


def get_products():

    return Products.objects.all().order_by('name')