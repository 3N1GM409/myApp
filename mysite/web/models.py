from django.db import models

# Create your models here.
class contact(models.Model):
        firstName = models.CharField(max_length=122)
        lastName = models.CharField(max_length=122)
        email = models.EmailField(max_length=254)
        message = models.CharField(max_length=122)
        docs= models.FileField(upload_to='uploads/')
        