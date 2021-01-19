from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Person, Photos
from .Serializers import PersonSerializer


class PersonInfo(ListAPIView):
    lookup_url_kwarg = "personId"
    serializer_class = PersonSerializer

    def get_queryset(self):
        personId = self.kwargs.get(self.lookup_url_kwarg)
        return Person.objects.get(id=personId)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PersonSerializer(queryset)
        return Response(serializer.data)
