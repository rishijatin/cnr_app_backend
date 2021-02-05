from rest_framework import serializers
from .models import healthCategory, Doctor, Photos


class HealthCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = healthCategory
        fields = ['id', 'name']


class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'doctor_name', 'doctor_photo']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ['id', 'url']


class DoctorDetailSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'doctor_photo', 'photos','video_url', 'doctor_name', 'qualification', 'experience', 'description']
