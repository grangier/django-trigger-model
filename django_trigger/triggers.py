"""

"""
from django.core.exceptions import ImproperlyConfigured


class TriggerAction(object):
    """

    """

    fields = {}
    signals = {}

    def __init__(self):

        classname = self.__class__.__name__

        # check fields
        if not isinstance(self.fields, dict):
            raise ImproperlyConfigured(
                '%s fields must be a dict' % classname
            )

        for k, v in self.fields.items():
            if not isinstance(v, list):
                raise ImproperlyConfigured(
                '%s fields["%s"] must be a list' % (classname, v)
            )

        # check signals:
        if not isinstance(self.signals, dict):
            raise ImproperlyConfigured(
                '%s signals must be a dict' % classname
            )

        for k, v in self.signals.items():
            if not isinstance(v, list):
                raise ImproperlyConfigured(
                '%s signals["%s"] must be a list' % (classname, k)
            )

        super(TriggerAction, self).__init__()

    @property
    def protected(self):
        return [
            'pre_init',
            'post_init',
            'post_syncdb',
            'class_prepared',
            #'m2m_changed'
    ]

    def get_callbacks(self, signal_type=None, changed_fields=[]):
        callbacks = []

        # check if there is actions registered to
        # this signal type
        if signal_type not in self.signals.keys():
            return callbacks

        for func_name in self.signals[signal_type]:
            if func_name in self.fields.keys():
                fields = set(self.fields[func_name])
                if fields.intersection(changed_fields):
                    func = getattr(self, func_name, None)
                    if func:
                        callbacks.append(func)

        return callbacks
