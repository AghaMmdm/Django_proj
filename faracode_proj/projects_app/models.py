from django.db import models

# Create your models here.

class project(models.Model):
    title = models.CharField(max_length=20, blank=True, null=False)
    description = models.TextField(max_length=25)
    address = models.CharField(max_length=400)
    image = models.ImageField(upload_to='project')

    def __str__(self):
        return self.title
