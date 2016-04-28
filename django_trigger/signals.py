

def trigger_signal(action, *args, **kwargs):
    instance = kwargs['instance']
    instance.dispatch_tracker(action, *args, **kwargs)


def trigger_pre_save(*args, **kwargs):
    trigger_signal('pre_save', *args, **kwargs)


def trigger_post_save(*args, **kwargs):
    trigger_signal('post_save', *args, **kwargs)
    instance = kwargs['instance']
    setattr(instance, "__initial", instance._dict)


def trigger_pre_delete(*args, **kwargs):
    trigger_signal('pre_delete', *args, **kwargs)


def trigger_post_delete(*args, **kwargs):
    trigger_signal('post_delete', *args, **kwargs)


def trigger_m2m_changed(*args, **kwargs):
    trigger_signal('m2m_changed', *args, **kwargs)
