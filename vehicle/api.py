from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Category, Photos, Details
from .serializers import CategorySerializer, DetailsSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class DetailsView(ListAPIView):
    serializer_class = DetailsSerializer
    lookup_url_kwarg = "category_id"

    def get_queryset(self):
        category_id = self.kwargs.get(self.lookup_url_kwarg)
        item = Details.objects.get(id=category_id)
        return item

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = DetailsSerializer(queryset)
        return Response(serializer.data)
