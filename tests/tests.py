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
    def test_API_login(self):
        client = Client()
        response = client.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)
    def test_API_homepage_without_login(self):
        client = Client()
        response = client.get('http://localhost:8000/homepage')
        self.assertEqual(response.status_code, 302)
    def test_API_register(self):
        client = Client()
        response = client.post('http://localhost:8000/register', 
        json={
            'name':'Barbosa',
            'email': 'junio@python.com',
            'password':'marceloarthur',
            'confirmPassword':'marceloarthur'
        }
        )
        assert response.status_code == 200
    def test_model_created(self):
        user = User.objects.first()
        self.assertEqual(user.name, "marcelo")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.email, "marceloarthurb@gmail.com")

    def test_model_register(self):
        client = Client()
        login = client.post('http://localhost:8000/login',
        json={
            'email': 'marceloarthurb@gmail.com',
            'password':'marceloarthur'
        })
        homepage = client.get('http://localhost:8000/homepage')
        assert homepage.status_code == 200

        


    
        
    

        
