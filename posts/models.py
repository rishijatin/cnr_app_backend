from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15, unique=True)
    image_url = models.URLField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"


class BlogPost(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    heading = models.CharField(max_length=40)
    photo_url_small = models.URLField()
    photo_url_large = models.URLField()
    webpage_url = models.URLField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
