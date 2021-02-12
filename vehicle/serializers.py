from rest_framework import serializers
from .models import Category, Photos, Details


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ['id', 'url']


class DetailsSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Details
        fields = ['id', 'description', 'services', 'video_url', 'photos']
