from django.db import models

# Create your models here.

class Menu(models.Model):
    ID = models.IntegerField(max_length=5)
    Title=models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory= models.IntegerField(max_length=5)
