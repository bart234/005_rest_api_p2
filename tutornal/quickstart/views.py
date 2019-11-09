from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer

# Create your views here.
# viewsets is grouping all common behavior together

class UserViewSet(viewsets.ModelViewSet):
    """
    This is one of endpoints
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    This is another endpoint
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
