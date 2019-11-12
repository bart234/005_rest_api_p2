from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Movie, Person
from .serializers import PersonSerializer
# Create your tests here.

class BaseViewTest(APITestCase):
    client = APIClient()


    @staticmethod
    def create_person(fname="", lname=""):
        if fname != "" and lname != "":
            Person.objects.create(fname=fname, lname=lname)

    def setUp(self):
        #add test data
        self.create_person("Olaf","Lubaszenko")
        self.create_person("Janina","Zablocka")
        self.create_person("Jarek","Karczor")
        self.create_person("Ola","Rosma")


class GetAllPersonsTest(BaseViewTest):

    def test_get_all_person(self):
        response = self.client.get(
            reverse('person-all-test', kwargs={"version","v1"})
        )

        expected = Person.objects.all()
        serialized = PersonSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

