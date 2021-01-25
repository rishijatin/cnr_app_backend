from django.db import models


# Create your models here.
class Contact(models.Model):
    phoneNo1 = models.CharField(max_length=15)
    phoneNo2 = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f'{self.id}'

