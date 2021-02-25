from django.test import TestCase, Client
import pytest
from america_app.models import User

class AmericaLineTest(TestCase):
    @classmethod
    def setUpTestData(self):
        User.objects.create(
            name = "marcelo",
            password = "password", 
            email = "marceloarthurb@gmail.com"
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
    def test_model_update(self):
        user = User.objects.update(
            name = "m",
            password = "p", 
            email = "m@gmail.com"
        )
        self.assertEqual(user.name, "m")
        self.assertEqual(user.password, "p")
        self.assertEqual(user.email, "m@gmail.com")
        
    

        
