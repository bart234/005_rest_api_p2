
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quickstart import views

"""
Because we're using viewsets instead of views, we can automatically generate
the URL conf for our API, by simply registering the viewsets with a router class.
"""
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
