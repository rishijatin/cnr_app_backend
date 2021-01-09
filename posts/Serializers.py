from rest_framework import serializers
from .models import Category, BlogPost


class CategoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image_url']


class BlogPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'heading', 'category', 'photo_url_small']
