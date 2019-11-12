from rest_framework import generics
from .models import Person
from movies.serializers import PersonSerializer

# Create your views here.

class ListPersons(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
