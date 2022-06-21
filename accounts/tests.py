from django.test import TestCase
from django.contrib.auth import get_user_model

class AccountsTests(TestCase):
    email = 'test@example.com'
    username = 'testuser'
    password = 'testpassword123'
    city = 'testcity'

    def test_create_user(self):
        user = get_user_model().objects.create(
            email=self.email,
            username=self.username,
            password=self.password,
            city=self.city,
        )
        self.assertEqual(user.email, self.email)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.city, self.city)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            email=self.email,
            username=self.username,
            password=self.password,
            city=self.city,
        )
        self.assertEqual(user.email, self.email)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.city, self.city)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

