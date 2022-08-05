from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class AccountsTests(TestCase):
    email = 'test@example.com'
    password = 'testpassword123'

    def test_create_user(self):
        user = get_user_model().objects.create(
            email=self.email,
            password=self.password,

        )
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            email=self.email,
            password=self.password,
        )
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

class SignUpTest(TestCase):

    email = 'test@example.com'
    password = 'testpassword123'
    
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