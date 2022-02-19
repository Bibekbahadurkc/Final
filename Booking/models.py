from django.db import models
from django.conf import settings


from django.utils.datetime_safe import datetime
from django.utils.timezone import now


# Create your models here.
from Pricing.models import Price


class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    priced = models.ForeignKey(Price, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, editable=False, )