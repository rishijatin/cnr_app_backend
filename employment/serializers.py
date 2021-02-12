from rest_framework import serializers
from .models import Category, Photo, EmploymentNews


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'url']


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentNews
        fields = ['id', 'heading']


class NewsDetailSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = EmploymentNews
        fields = ['id', 'heading', 'description', 'location', 'details', 'video_url', 'photos']
