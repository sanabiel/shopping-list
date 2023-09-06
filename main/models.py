from django.db import models

# Create my models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
