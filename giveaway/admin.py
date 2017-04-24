from django.contrib import admin
from .models import Category, Prize, Giveaway

# Register your models here.
admin.site.register(Category)
admin.site.register(Prize)
admin.site.register(Giveaway)
