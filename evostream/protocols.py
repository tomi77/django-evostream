from base64 import b64encode
import json
import socket
try:
    from httplib import HTTPConnection
except ImportError:
    from http.client import HTTPConnection

from .conf import settings
from . import EvoStreamException


class BaseProtocol(object):
    def get_result(self, command, **params):
        raise NotImplementedError()

    def parse_result(self, result):
        raise NotImplementedError()

    def execute(self, command, **params):
        result = self.get_result(command, **params)

        return self.parse_result(result)


class HTTPProtocol(BaseProtocol):
    @staticmethod
    def make_uri(command, **params):
        uri = '/%s' % command
        if len(params) > 0:
            str_params = ' '.join(['%s=%s' % (i, params[i]) for i in params])
            uri += '?params=%s' % b64encode(str_params)
        return uri

    def get_result(self, command, **params):
        conn = HTTPConnection(settings.EVOSTREAM_URL)
        uri = self.make_uri(command, **params)
        try:
            conn.request('GET', uri)
        except socket.error as ex:
            raise EvoStreamException(ex)
        response = conn.getresponse()
        return response.read()

    def parse_result(self, result):
        result = json.loads(result)
        if result['status'] == 'FAIL':
            raise EvoStreamException(result['description'])
        else:
            return result['data']
