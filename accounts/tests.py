from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class AccountsTests(TestCase):
    username = 'testusername'
    email = 'test@example.com'
    first_name = 'testuser'
    last_name = 'testuser1'
    password = 'testpassword123'
    city = 'testcity'

    def test_create_user(self):
        user = get_user_model().objects.create(
            email=self.email,
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            password=self.password,
            city=self.city,
        )
        self.assertEqual(user.email, self.email)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.first_name, self.first_name)
        self.assertEqual(user.last_name, self.last_name)
        self.assertEqual(user.city, self.city)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            email=self.email,
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            password=self.password,
            city=self.city,
        )

        self.assertEqual(user.email, self.email)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.first_name, self.first_name)
        self.assertEqual(user.last_name, self.last_name)
        self.assertEqual(user.city, self.city)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

class SignUpTest(TestCase):

    email = 'test@example.com'
    first_name = 'testuser'
    last_name = 'testuser1'
    password = 'testpassword123'
    city = 'testcity'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')

    def test_signup_form(self):
        new_user = get_user_model().objects.create(
            email=self.email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)