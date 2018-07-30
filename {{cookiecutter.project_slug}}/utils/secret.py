import os

from django.core.exceptions import ImproperlyConfigured


def get(setting, fallback=None, fallback_dict=None):
    if os.environ.get(setting):
        return os.environ[setting]
    else:
        try:
            return fallback_dict[setting]
        except KeyError:
            if fallback is not None:
                return fallback

            raise ImproperlyConfigured('The setting {} was not found in your environment'.format(setting))
