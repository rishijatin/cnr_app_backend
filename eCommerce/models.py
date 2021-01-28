from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "e Commerce Categories"

    def __str__(self):
        return f'{self.id}: {self.name}'


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    small_image_url = models.URLField()
    large_image_url = models.URLField()
    website_url = models.URLField()
    price = models.CharField(max_length=50,blank=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.id}: {self.name}'


class PhotoItem(models.Model):
    url = models.URLField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}-{self.url}'
