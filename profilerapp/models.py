from django.db import models

# Create your models here.
class Users(models.Model):
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=200)
    images = models.ImageField(default="background21.png")

    def __str__(self):
        return self.email