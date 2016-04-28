"""
Django Trigger models
"""
import logging

from django.db.models import signals

from django_trigger.diffmodelmixin import ModelDiffMixin
from django_trigger.triggers import TriggerAction
from django_trigger import signals as trigger_signals


logger = logging.getLogger(__name__)


class TriggerModel(ModelDiffMixin):

    _triggers = TriggerAction()

    class Meta:
        abstract = True

    def dispatch_tracker(self, signal_type, *args, **kwargs):
        # changed field
        changed_fields = self.changed_fields
        if not changed_fields:
            return

        callbacks = self._triggers.get_callbacks(signal_type, changed_fields)

        for callback in callbacks:
            try:
                callback(*args, **kwargs)
            except Exception as e:
                msg = "%s : %s" % (callback.__name__, e)
                logger.error(msg)
                continue


def subscribe_to_tracker(sender, **kwargs):
    if issubclass(sender, TriggerModel):
        for signal in sender._triggers.signals.keys():

            # we don't handle pre_init
            if signal in sender._triggers.protected:
                continue

            if hasattr(signals, signal):
                # dispatch uid
                dispatch_uid = "{0}_trigger.{1}.{2}".format(
                    signal,
                    sender.__module__,
                    sender.__name__
                )

                # signal
                sig = getattr(signals, signal)
                func = getattr(trigger_signals, 'trigger_%s' % signal, None)
                if func:
                    sig.connect(
                        func,
                        sender=sender,
                        weak=False,
                        dispatch_uid=dispatch_uid
                    )

# subscripe class_prepared signal
signals.class_prepared.connect(subscribe_to_tracker)
