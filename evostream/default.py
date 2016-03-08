try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

from django.utils.functional import LazyObject

from .conf import settings
from .utils import get_module_class


SCHEMES = {
    'http': 'evostream.protocols.HTTPProtocol',
    'telnet': 'evostream.protocols.TelnetProtocol',
}


class Protocol(LazyObject):
    def _setup(self):
        url = urlparse.urlparse(settings.EVOSTREAM_URI)
        protocol_class = get_module_class(SCHEMES[url.scheme])
        self._wrapped = protocol_class('%s:%d' % (url.hostname, url.port))

protocol = Protocol()
