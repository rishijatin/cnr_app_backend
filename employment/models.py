from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.id}-{self.name}'


class EmploymentNews(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)
    description = models.TextField()
    location = models.TextField()
    details = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    video_url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'Employment News'

    def __str__(self):
        return f'{self.id}-{self.heading}'


class Photo(models.Model):
    url = models.URLField()
    news = models.ForeignKey(EmploymentNews, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return f'{self.id}-{self.news.heading} photo'
