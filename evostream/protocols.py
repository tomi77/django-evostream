from base64 import b64encode
import json
import socket

from django.conf import settings

try:
    from httplib import HTTPConnection
except ImportError:
    from http.client import HTTPConnection


class BaseProtocol(object):
    def execute(self, command, params=None):
        raise NotImplementedError()


class HTTPProtocol(BaseProtocol):
    def execute(self, command, params=None):
        conn = HTTPConnection(settings.EVOSTREAM_URL)
        if params is None:
            uri = '/%s' % command
        else:
            str_params = ' '.join(['%s=%s' % (i, params[i]) for i in params])
            uri = '/%s?params=%s' % (command, b64encode(str_params))
        try:
            conn.request('GET', uri)
        except socket.error as ex:
            raise ConnectionError(ex)
        response = conn.getresponse()
        return json.loads(response.read())
