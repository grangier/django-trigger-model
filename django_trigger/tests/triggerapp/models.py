from django.db import models

from django_trigger.models import TriggerModel
from django_trigger.tests.triggerapp.triggers import SectionTriggerAction
from django_trigger.tests.triggerapp.triggers import ArticleTriggerAction


class Article(TriggerModel):
    title = models.CharField(max_length=250)

    _triggers = ArticleTriggerAction()


class Section(TriggerModel):
    title = models.CharField(max_length=250)
    articles = models.ManyToManyField(Article)

    _triggers = SectionTriggerAction()


class TriggerLog(models.Model):
    action = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
