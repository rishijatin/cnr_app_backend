from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import healthCategory, Doctor
from .serializers import HealthCategorySerializer, DoctorListSerializer, DoctorDetailSerializer


class CategoryView(ListAPIView):
    queryset = healthCategory.objects.all()
    serializer_class = HealthCategorySerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = HealthCategorySerializer(queryset, many=True)
        return Response(serializer.data)


class DoctorListView(ListAPIView):
    serializer_class = DoctorListSerializer
    lookup_url_kwarg = "category_id"

    def get_queryset(self):
        category_id = self.kwargs.get(self.lookup_url_kwarg)
        posts = Doctor.objects.filter(category=category_id)
        return posts

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # page = self.paginate_queryset(queryset)
        # serializer = ItemListSerializer(page, many=True)
        # return self.get_paginated_response(serializer.data)
        serializer = DoctorListSerializer(queryset, many=True)
        return Response(serializer.data)


class DoctorDetailView(ListAPIView):
    serializer_class = DoctorDetailSerializer
    lookup_url_kwarg = "doctor_id"

    def get_queryset(self):
        item_id = self.kwargs.get(self.lookup_url_kwarg)
        post = Doctor.objects.get(id=item_id)
        return post

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = DoctorDetailSerializer(queryset)
        return Response(serializer.data)
