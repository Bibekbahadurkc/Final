from django.db import models

# Create your models here.
class Price(models.Model):
    name = models.CharField(max_length=200)
    image=models.ImageField(upload_to='Media')
    features = models.CharField(max_length=200)
    prices = models.IntegerField()