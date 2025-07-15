from django.db import models

# Create your models here.

class footer(models.Model):
    addres = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    whatsapp = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)

class message(models.Model):
    fname = models.CharField(max_length=50)
    email = models.EmailField()
    sub = models.CharField(max_length=50)
    bdy = models.TextField()

    def __str__(self):
        return self.fname + " : " + self.sub