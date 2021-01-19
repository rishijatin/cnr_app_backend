from rest_framework import serializers
from .models import healthCategory, Doctor


class HealthCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = healthCategory
        fields = ['id', 'name']


class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'doctor_name', 'doctor_photo']


class DoctorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'doctor_photo', 'doctor_name', 'qualification', 'experience', 'description']
