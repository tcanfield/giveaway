from django.shortcuts import render
from .models import Prize

# Create your views here.

def giveaway_list(request):
    active_prizes = Prize.objects.filter(end_date=None);
    return render(request, 'giveaway/giveaway_list.html', {'active_prizes': active_prizes})
