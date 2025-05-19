from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RegistrationViewTests(TestCase):
    def test_register_creates_user(self):
        response = self.client.post(reverse('register-users'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())


class ProfileViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user', email='old@example.com', password='pass12345'
        )

    def test_profile_update(self):
        self.client.login(username='user', password='pass12345')
        response = self.client.post(reverse('profile'), {
            'username': 'updated',
            'email': 'new@example.com',
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updated')
        self.assertEqual(self.user.email, 'new@example.com')


class UserSearchViewTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass123')
        self.user2 = User.objects.create_user(username='otheruser', password='pass123')

    def test_search_returns_user(self):
        self.client.login(username='user1', password='pass123')
        response = self.client.post(reverse('search'), {'search': 'other'})
        self.assertEqual(response.status_code, 200)
        results = list(response.context['results'])
        self.assertIn(self.user2, results)
