from django.core.validators import MaxValueValidator
from django.db import models

class Booking(models.Model):
    ID = models.BigIntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(validators=[MaxValueValidator(999999)])
    BookingDate = models.DateTimeField()
    
class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(validators=[MaxValueValidator(99999)])
