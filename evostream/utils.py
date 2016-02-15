from importlib import import_module

from django.core.exceptions import ImproperlyConfigured


def get_module_class(class_path):
    """
    imports and returns module class from ``path.to.module.Class``
    argument
    """
    mod_name, cls_name = class_path.rsplit('.', 1)

    try:
        mod = import_module(mod_name)
    except ImportError as ex:
        raise ImproperlyConfigured('Error importing module %s: "%s"' % (mod_name, ex))

    return getattr(mod, cls_name)
