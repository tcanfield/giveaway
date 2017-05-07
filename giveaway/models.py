from django.db import models
import random, math, datetime
# Create your models here.
class Category(models.Model):
    parent_category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField()
    description = models.TextField()

    def get_all_sub_categories(self):
        all_sub_categories = []
        for sub_category in Category.objects.filter(parent_category=self):
            all_sub_categories.append(sub_category)
            sub_category.get_all_sub_categories()
        return all_sub_categories

    def __str__(self):
        return self.name

class Prize(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to = 'static/images')
    description = models.TextField()
    link = models.URLField()
    referral_link = models.URLField()
    value = models.DecimalField(max_digits=999, decimal_places=2)

    def __str__(self):
        return self.name

class Giveaway(models.Model):
    name = models.TextField()
    description = models.TextField()
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.datetime.now)
    end_time = models.DateTimeField(blank=True, null=True)
    odds = models.DecimalField(max_digits=999, decimal_places=999)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    attempts = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def rollToWin(self):
        min = 1
        max = math.ceil(1 / self.odds)
        winningNum = random.randint(min, max)
        rolledNum = random.randint(min, max)
        if(rolledNum == winningNum):
            return True
        else:
            return False

    def start(self):
        self.start_time = datetime.datetime.now()
        self.save()

    def end(self):
        self.end_time = datetime.datetime.now()
        self.save()

class Entry(models.Model):
    giveaway = models.ForeignKey(Giveaway)
    email_address = models.EmailField()
    attempts = models.PositiveIntegerField(default=1)
    winner = models.BooleanField(default=False)
