from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


# Custom User Model
class User(models.Model):
    pass
