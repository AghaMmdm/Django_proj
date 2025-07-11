from django.db import models

# Create your models here.


class course(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    status = models.BooleanField(default= False)
    views = models.IntegerField(null= True)
    
    def __str__(self):
        return self.title