from rest_framework import generics
from .models import Faq
from .serializers import FaqSerializer

# List all FAQs or create a new FAQ
class FaqListCreate(generics.ListCreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

# Retrieve, update, or delete an FAQ
class FaqRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

