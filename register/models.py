from django.db import models

# Create your models here.


class Registration(models.Model):
    bsc_address = models.CharField(max_length=200,primary_key=True)
    nami_address = models.CharField(max_length=200,null=True,blank=True)
    register_date = models.DateTimeField('date registered',auto_now_add=True, blank=True)

    def __str__(self):
        return self.bsc_address


class Reservation(models.Model):
    slot_number = models.IntegerField()
    address = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    amount_BNB = models.FloatField()