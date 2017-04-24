from django.shortcuts import render
from .models import Giveaway, Prize, Category

# Create your views here.

def giveaway_list(request):
    active_giveaways = Giveaway.objects.filter(end_time=None)
    return render(request, 'giveaway/giveaway_list.html', {'active_giveaways': active_giveaways})
