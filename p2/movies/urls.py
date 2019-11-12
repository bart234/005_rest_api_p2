from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from movies import views

urlpatterns = [
    path('api/', views.ListPersons.as_view()),
    path('api/<int:pk>/', views.DetailPerson.as_view()),
]