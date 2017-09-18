import os


def get_settings_module():
    if os.path.is_file('settings_module'):
        with open('settings_module', 'r') as f:
            return f.read().strip()


def set_settings_module():
    if 'DJANGO_SETTINGS_MODULE' not in os.environ:
        settings_module = get_settings_module()

        if settings_module:
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
