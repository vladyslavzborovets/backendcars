from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=32)
    make = models.CharField(max_length=32)
    image = models.CharField(max_length=700)
    made_by = models.CharField(max_length=32)
    hp = models.IntegerField()
    history_of_productions = models.CharField(max_length=800)

# Create your models here.
