from django.test import TestCase

from .models import Techniques
from django.urls import reverse

class QuizIndexViewTests(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('quiz:index'))
        self.assertEqual(response.status_code, 200)