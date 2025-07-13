from django.db import models

# Create your models here.


class course(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    status = models.BooleanField(default= False)
    views = models.IntegerField(default= 0)
    image = models.ImageField(null= True, upload_to="courses_images")
    
    def __str__(self):
        return self.title