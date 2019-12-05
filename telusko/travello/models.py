from django.db import models

# Create your models here.
class Destination(models.Model):
    #objects = models.Manager()
    name= models.CharField(max_length= 100)
    img= models.ImageField(upload_to= 'pics')
    desc= models.TextField()
    price= models.IntegerField()
    specialoffer= models.BooleanField(default=False)
