from django.shortcuts import render
from .models import Giveaway, Prize, Category, Entry

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

def giveaway(request, pk):
    giveaway = Giveaway.objects.get(pk=pk)
    return render(request, 'giveaway/giveaway.html', {'giveaway': giveaway})

def enter_giveaway(request, giveaway_id):
    giveaway = Giveaway.objects.get(pk=giveaway_id)
    giveaway.attempts += 1
    email_address = request.POST['email_address']
    entry = Entry.objects.filter(giveaway = giveaway).filter(email_address = email_address).first() #TODO giveaway and email should be primary key

    if not entry:
        entry = Entry(giveaway=giveaway, email_address=email_address)
    else:
        entry.attempts += 1

    is_winner = giveaway.rollToWin()
    if(is_winner):
        entry.winner = True
        giveaway.end()

    giveaway.save()
    entry.save()

    return render(request, 'giveaway/enter_giveaway.html', {'giveaway':giveaway, 'entry':entry})
