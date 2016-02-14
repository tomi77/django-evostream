from django.utils.functional import LazyObject

from .conf import settings
from .utils import get_module_class


class Protocol(LazyObject):
    def _setup(self):
        self._wrapped = get_module_class(settings.EVOSTREAM_PROTOCOL)()

protocol = Protocol()
