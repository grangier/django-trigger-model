from django.test import TestCase

from django_trigger.tests.triggerapp.models import Article
from django_trigger.tests.triggerapp.models import Section


class TriggerTest(TestCase):

    def setUp(self):
        Article.objects.create(title="article test")

    def test_one(self):
        self.assertEqual('yo', 'yo')
