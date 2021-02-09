from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.id}-{self.name}'


class Function(models.Model):
    name = models.CharField(max_length=100)
    invitation_card = models.URLField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    date_added = models.DateTimeField(auto_now_add=True)
    video_url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'{self.id}-{self.name}'


class Photos(models.Model):
    function = models.ForeignKey(Function, on_delete=models.CASCADE, related_name='photos')
    url = models.URLField()

    class Meta:
        verbose_name_plural = 'Photos'

    def __str__(self):
        return f'{self.id}'
