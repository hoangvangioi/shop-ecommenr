from django.shortcuts import render
from .models import Category
from django.db.models import Q


# Create your views here.

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            category = Category.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            category_count = category.count()
    context = {
        'category': category,
        'category_count': category_count,
    }
    return render(request, 'home.html', context)