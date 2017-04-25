from django.shortcuts import render
from .models import Giveaway, Prize, Category

# Create your views here.
def category_list(request):
    parent_categories = Category.objects.filter(parent_category=None)
    return render(request, 'giveaway/category_list.html', {'parent_categories': parent_categories})

def giveaway_list(request, pk):
    all_categories = []
    parent_category = Category.objects.get(pk=pk)
    all_categories.append(parent_category)
    sub_categories = parent_category.get_all_sub_categories()
    all_categories.extend(sub_categories)

    active_giveaways = Giveaway.objects.filter(end_time=None).filter(category__in=all_categories)
    return render(request, 'giveaway/giveaway_list.html', {'active_giveaways': active_giveaways})
