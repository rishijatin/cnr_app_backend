from django.contrib import admin
from .models import healthCategory, Doctor,Photos

# Register your models here.
admin.site.register(healthCategory)
admin.site.register(Doctor)
admin.site.register(Photos)