from django.shortcuts import render
from django.db.models import Sum   

from myapp5.models import Product


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title':'Общее количество посчитанно в базе данных',
        'total': total,
        
    }
    return render(request, 'myapp6/total_count.html', context)
def total_in_tamplate(request):
    context={
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 'myapp6/total_count.html', context)