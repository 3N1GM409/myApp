from django.db import models
# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    file = models.FileField(upload_to='Pictures/', default=None)
    message = models.CharField(max_length=122)

    def __str__(self):
        return self.first_name
    