import json
try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

from django.core.management import call_command
from django.test import TestCase
from evostream import EvoStreamException
from evostream.protocols import BaseProtocol


class TestProtocol(BaseProtocol):
    def __init__(self, result):
        self.result = result

    def get_result(self, command, **params):
        return self.result

    def parse_result(self, result):
        result = json.loads(result)
        if result['status'] == 'FAIL':
            raise EvoStreamException(result['description'])
        else:
            return result['data']


LIST_STREAMS_IDS_TEST_DATA = {
    "data": [205, 206, 207],
    "description": "Available stream IDs",
    "status": "SUCCESS"
}


class ListStreamsIdsTestCase(TestCase):
    @patch('evostream.commands.protocol', TestProtocol(json.dumps(LIST_STREAMS_IDS_TEST_DATA)))
    def test_success(self):
        from evostream.commands import list_streams_ids
        ids = list_streams_ids()
        self.assertListEqual(ids, LIST_STREAMS_IDS_TEST_DATA['data'])


class ListStreamsIdsCommandTestCase(TestCase):
    @patch('evostream.commands.protocol', TestProtocol(json.dumps(LIST_STREAMS_IDS_TEST_DATA)))
    @patch('sys.stdout.write')
    def test_command(self, mock_write):
        call_command('liststreamsids')
        self.assertEqual(mock_write.call_count, 1)
        self.assertEqual(mock_write.call_args,
                         [(json.dumps(LIST_STREAMS_IDS_TEST_DATA['data'], indent=1, sort_keys=True) + '\n', )])
