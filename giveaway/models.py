from django.db import models
import datetime
# Create your models here.

class Prize(models.Model):
    name = models.TextField()
    start_date = models.DateTimeField(default=datetime.datetime.now)
    end_date = models.DateTimeField(blank=True, null=True)
    odds = models.DecimalField(max_digits=999, decimal_places=999)
    item_link = models.TextField()
    referral_link = models.TextField()
    value = models.DecimalField(max_digits=999, decimal_places=2)

    def end(self):
        self.end_date = datetime.datetime.now()
        self.save()

    def __str__(self):
        return self.name
