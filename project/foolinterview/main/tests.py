from django.test import TestCase, Client
from django.urls import reverse

class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')

    def test_article(self):
        url = reverse('article', kwargs={'uuid':'a7acd8c8-c5ce-11e7-9fa6-0050569d4be0'})
        print(url)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/article.html')