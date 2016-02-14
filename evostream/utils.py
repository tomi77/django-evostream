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


def check_params(expected, got):
    if not isinstance(expected, set):
        expected = set(expected)
    if not isinstance(got, set):
        got = set(got)
    if bool(got - expected):
        unexpected = ','.join([key for key in list(got - expected)])
        raise KeyError('Unexpected argument(s): %s' % unexpected)
