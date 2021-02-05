from django.db import models


# Create your models here.
class healthCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Health Categories"

    def __str__(self):
        return f'{self.id}-{self.name}'


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=50)
    video_url = models.URLField()
    description = models.TextField()
    doctor_photo = models.URLField()
    experience = models.IntegerField(default=0)
    qualification = models.TextField()
    category = models.ForeignKey(healthCategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ["doctor_name"]

    def __str__(self):
        return f'{self.id} - {self.doctor_name}'

    class Photos(models.Model):
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='photos')
