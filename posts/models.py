from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=15, unique=True)
    description = models.TextField(null=True)
    image_url = models.URLField()
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.id}: {self.name}'


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

    def __str__(self):
        return f'{self.id}: {self.heading}'
