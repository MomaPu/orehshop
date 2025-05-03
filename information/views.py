
from django.shortcuts import render


from information.models import Information

def shop_info(request):
    info = Information.objects.all()
    context = {
        'info': info
    }
    return render(request, "shop_info.html", context)
