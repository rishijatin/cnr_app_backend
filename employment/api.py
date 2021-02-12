from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Category, Photo, EmploymentNews
from .serializers import CategorySerializer, NewsListSerializer, NewsDetailSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class NewsListView(ListAPIView):
    serializer_class = NewsListSerializer
    lookup_url_kwarg = "category_id"

    def get_queryset(self):
        category_id = self.kwargs.get(self.lookup_url_kwarg)
        articles = EmploymentNews.objects.filter(id=category_id)
        return articles

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = NewsListSerializer(queryset, many=True)
        return Response(serializer.data)


class NewsDetailView(ListAPIView):
    serializer_class = NewsDetailSerializer
    lookup_url_kwarg = "article_id"

    def get_queryset(self):
        article_id = self.kwargs.get(self.lookup_url_kwarg)
        article = EmploymentNews.objects.get(id=article_id)
        return article

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = NewsDetailSerializer(queryset)
        return Response(serializer.data)
