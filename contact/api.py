from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer


class ContactView(ListAPIView):

    serializer_class = ContactSerializer

    def get_queryset(self):
        contact = Contact.objects.get(id=1)
        return contact

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ContactSerializer(queryset)
        return Response(serializer.data)
