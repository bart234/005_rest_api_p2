from rest_framework import serializers
from movies.models import Person, Movie

class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Person
        fields = ("pk","fname","lname")