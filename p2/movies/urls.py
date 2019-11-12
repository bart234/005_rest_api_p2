from django.urls import path
from .views import ListPersons


urlpatterns = [
    path('p/', ListPersons.as_view(), name="person-all")
]