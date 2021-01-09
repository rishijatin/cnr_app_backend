from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Category, BlogPost
from .Serializers import (BlogPostListSerializer, CategoryGetSerializer,
                          BlogPostDetailSerializer)


class CustomPaginator(PageNumberPagination):
    page_size = 1
    page_query_param = 'page_size'
    max_page_size = 100


class ListCategories(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryGetSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategoryGetSerializer(queryset, many=True)
        return Response(serializer.data)


class BlogPostList(ListAPIView):
    serializer_class = BlogPostListSerializer
    lookup_url_kwarg = "category_id"
    pagination_class = CustomPaginator

    def get_queryset(self):
        category_id = self.kwargs.get(self.lookup_url_kwarg)
        posts = BlogPost.objects.filter(category=category_id)
        return posts

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = BlogPostListSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class BlogPostDetail(ListAPIView):
    serializer_class = BlogPostDetailSerializer
    lookup_url_kwarg = "item_id"

    def get_queryset(self):
        item_id = self.kwargs.get(self.lookup_url_kwarg)
        post = BlogPost.objects.get(id=item_id)
        return post

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BlogPostDetailSerializer(queryset)
        return Response(serializer.data)
