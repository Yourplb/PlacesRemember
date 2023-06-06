from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Impressions
from .forms import ImpressionsForm


class ImpressionsCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'testuser@mail.com', 'testpass')
        self.client.login(username='testuser', password='testpass')
        self.url = reverse('impressions:impressions_create')

    def test_create_impressions(self):

        data = {
            'title': 'Test Impressions',
            'description': 'Test Description',
            'location': '56.006875653960066,92.85331249237062'
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Impressions.objects.filter(title='Test Impressions').exists())

    def test_create_impressions_invalid_form(self):

        data = {
            'title': '',
            'description': 'Test Description',
            'location': '56.006875653960066,92.85331249237062'
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'title', 'Обязательное поле.')


class ImpressionsListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'testuser@mail.com', 'testpass')
        self.client.login(username='testuser', password='testpass')
        self.url = reverse('impressions:impressions')

    def test_impressions_list(self):
        impressions = Impressions.objects.create(
            author=self.user,
            title='Test Impressions',
            description='Test Description',
            location='56.006875653960066,92.85331249237062'
        )

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['impressions'], ['Test Impressions'], transform=str)
        self.assertContains(response, 'Test Impressions')
