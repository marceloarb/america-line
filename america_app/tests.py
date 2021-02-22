from django.test import TestCase, Client
from .models import *

class AmericaLineTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            name = "marcelo",
            password = "password", 
            email = "marceloarthurb@gmail.com",

        )
    def test_API_login_page(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)
    def test_model_create(self):
        user = User.objects.first()
        self.assertEqual(user.name, "marcelo")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.email, "marceloarthurb@gmail.com")
    def test_model_delete(self):
        user = User.objects.first()
        self.assertEqual(user.name, null)

        
