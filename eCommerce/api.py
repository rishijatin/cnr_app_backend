from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Item, Category
from .serializers import CategorySerializer, ItemListSerializer, ItemDetailSerializer


class CustomPaginator(PageNumberPagination):
    page_size = 1
    page_query_param = 'page_size'
    max_page_size = 100


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ItemListView(ListAPIView):
    serializer_class = ItemListSerializer
    lookup_url_kwarg = "category_id"
    pagination_class = CustomPaginator

    def get_queryset(self):
        category_id = self.kwargs.get(self.lookup_url_kwarg)
        posts = Item.objects.filter(category=category_id)
        return posts

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # page = self.paginate_queryset(queryset)
        # serializer = ItemListSerializer(page, many=True)
        # return self.get_paginated_response(serializer.data)
        serializer = ItemListSerializer(queryset,many=True)
        return Response(serializer.data)


class ItemDetailView(ListAPIView):
    serializer_class = ItemDetailSerializer
    lookup_url_kwarg = "item_id"

    def get_queryset(self):
        item_id = self.kwargs.get(self.lookup_url_kwarg)
        post = Item.objects.get(id=item_id)
        return post

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ItemDetailSerializer(queryset)
        return Response(serializer.data)
