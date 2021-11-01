from django.db import models

# Create your models here.


class Registration(models.Model):
    bsc_address = models.CharField(max_length=200)
    nami_address = models.CharField(max_length=200,null=True,blank=True)
    register_date = models.DateTimeField('date registered',auto_now_add=True, blank=True)

    def __str__(self):
        return self.bsc_address