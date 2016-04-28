from django_trigger.triggers import TriggerAction


class ArticleTriggerAction(TriggerAction):

    fields = {
        '_change_title': [
            'title'
        ]
    }

    signals = {
        'post_save': [
            '_change_title'
        ]
    }

    def _change_title(self):
        print "_change_title"
        #from django_trigger.tests.models import TriggerLog
        #TriggerLog


class SectionTriggerAction(TriggerAction):

    fields = {
        '_change_title': [
            'title'
        ]
    }

    signals = {
        'post_save': [
            '_change_title'
        ]
    }
