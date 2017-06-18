from django.shortcuts import render, redirect
from django.core.mail import send_mail
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
    return render(request, 'giveaway/giveaway_list.html', {'active_giveaways': active_giveaways, 'parent_category':parent_category})

def giveaway(request, pk):
    giveaway = Giveaway.objects.get(pk=pk)
    return render(request, 'giveaway/giveaway.html', {'giveaway': giveaway})


def enter_giveaway_result(request, giveaway_id, entry_id):
    giveaway = Giveaway.objects.get(pk=giveaway_id)
    entry = Entry.objects.get(pk=entry_id)
    winning_numbers = giveaway.rollWinningNumbers()
    if(entry.winner):
        rolled_numbers = winning_numbers
    else:
        rolled_numbers = giveaway.rollNumbers()
        #TODO this will not work if there is only one possible roll, This will need to change if a 100% win rate is ever needed
        while(rolled_numbers == winning_numbers):
            rolled_numbers = giveaway.rollNumbers()
    return render(request, 'giveaway/enter_giveaway.html', {'giveaway':giveaway, 'winning_numbers':winning_numbers, 'rolled_numbers':rolled_numbers, 'entry':entry})

def enter_giveaway(request, giveaway_id):
    giveaway = Giveaway.objects.get(pk=giveaway_id)
    giveaway.attempts += 1
    email_address = request.POST['email_address']
    entry = Entry.objects.filter(giveaway = giveaway).filter(email_address = email_address).first() #TODO giveaway and email should be primary key

    if not entry:
        entry = Entry(giveaway=giveaway, email_address=email_address)
    else:
        entry.attempts += 1

    is_winner = (giveaway.rollNumbers() == giveaway.rollWinningNumbers())
    if(is_winner):
        entry.winner = True
        giveaway.end()

    giveaway.save()
    entry.save()

    #Email winner
    if(is_winner):
        email_winner(entry)

    return redirect(enter_giveaway_result, giveaway.id, entry.id)

def email_winner(entry):
    if(entry.winner):
        address = entry.email_address;
        subject = "Congratulations"
        body = "Congratulations! You have won " + entry.giveaway.prize.name
        send_mail(subject, body, "testemail@testemail.com", [address])
