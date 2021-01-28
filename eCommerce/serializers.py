from rest_framework import serializers
from .models import Category, Item, PhotoItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'small_image_url', 'price']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoItem
        fields = ['id', 'url']


class ItemDetailSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)
    class Meta:
        model = Item
        fields = ['id', 'name', 'photos', 'price', 'description', 'website_url', 'category']
