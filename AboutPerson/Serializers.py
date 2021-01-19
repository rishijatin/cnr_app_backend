from rest_framework import serializers
from .models import Person, Photos


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ['id', 'url']


class PersonSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Person
        fields = ['id', 'name', 'description', 'social_work', 'family_members', 'photos']
