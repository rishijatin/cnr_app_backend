from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Category, Function, Photos
from .serializers import CategorySerializer, FunctionListSerializer, FunctionDetailSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class FunctionListView(ListAPIView):
    serializer_class = FunctionListSerializer
    lookup_url_kwarg = "category_id"

    def get_queryset(self):
        category_id = self.kwargs.get(self.lookup_url_kwarg)
        functions = Function.objects.filter(category=category_id)
        return functions

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = FunctionListSerializer(queryset, many=True)
        return Response(serializer.data)


class FunctionDetailView(ListAPIView):
    serializer_class = FunctionDetailSerializer
    lookup_url_kwarg = "item_id"

    def get_queryset(self):
        item_id = self.kwargs.get(self.lookup_url_kwarg)
        function = Function.objects.get(id=item_id)
        return function

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = FunctionDetailSerializer(queryset)
        return Response(serializer.data)