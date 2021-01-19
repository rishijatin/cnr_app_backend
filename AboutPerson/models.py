from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    social_work = models.TextField()
    family_members = models.TextField()

    class Meta:
        verbose_name_plural = "Person"

    def __str__(self):
        return f'{self.id}- {self.name}'


class Photos(models.Model):
    url = models.URLField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE,related_name="photos")

    def __str__(self):
        return f'{self.id}-{self.url}'

    class Meta:
        verbose_name_plural = "Photos"
