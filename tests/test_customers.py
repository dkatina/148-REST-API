import unittest
from faker import Faker
from app import create_app #import our application factory to create an instance of our app
from database import db
from unittest.mock import patch

class TestCustomer(unittest.TestCase):

    def setUp(self):
        app = create_app('TestingConfig')
        with app.app_context():
            db.create_all()
        self.app = app.test_client()

    def test_create_customer(self):
        fake = Faker()
        name = fake.name()
        phone = fake.basic_phone_number()
        username = fake.user_name()
        password = fake.password()
        email = fake.email()
        admin = 1

        payload = { #Creating customer payload from mocked data
            "name": name,
            "phone":phone,
            "username": username,
            "password": password,
            "email": email,
            "admin": admin
        }

        response = self.app.post('/customers/', json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], name)

    @patch('services.customerService.login') #Patching allows us to skip over a potentially hazardous function and keep moving down the chain
    def test_customer_login(self, mock_login):
        fake = Faker()
        response_object = "xlajsndg;lnqorwjnopjansdfvvuafsd,jngaidxbxvuyasding"

        mock_login.return_value = response_object

        payload = {
            'email': fake.email(),
            'password': fake.password()
        }
        

        response = self.app.post('/customers/login', json=payload)
        self.assertEqual(response.status_code, 200)

        

if __name__ == "__main__":
    unittest.main()