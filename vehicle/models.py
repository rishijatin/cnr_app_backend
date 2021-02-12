from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.id}-{self.name}'


class Details(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    services = models.TextField()
    video_url = models.URLField()

    class Meta:
        verbose_name_plural = 'Details'

    def __str__(self):
        return f'{self.id}-{self.category.name} details'


class Photos(models.Model):
    url = models.URLField()
    details = models.ForeignKey(Details, on_delete=models.CASCADE, related_name='photos')

    class Meta:
        verbose_name_plural='Photos'

    def __str__(self):
        return f'{self.id}-{self.details.category.name} related photo'
