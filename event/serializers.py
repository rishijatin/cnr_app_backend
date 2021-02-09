from rest_framework import serializers
from .models import Category, Function, Photos


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ['id', 'url']


class FunctionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Function
        fields = ['id', 'name']


class FunctionDetailSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Function
        fields = ['id', 'name', 'invitation_card', 'video_url', 'photos']
