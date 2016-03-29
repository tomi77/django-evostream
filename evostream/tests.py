import json
import os

import django

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

from django.core.management import call_command
from django.test import TestCase
from evostream.commands import list_streams_ids, get_stream_info, list_streams, get_streams_count
from evostream.protocols import HTTPProtocol


class TestHTTPProtocol(HTTPProtocol):
    def __init__(self, result):
        self.result = json.dumps(result)

    def get_result(self, command, **params):
        return self.result


def load_test_data(filename):
    return json.load(open(os.path.join('testapp', 'testdata', filename)))

LIST_STREAMS_IDS_TEST_DATA = load_test_data('list_streams_ids.json')


@patch('evostream.commands.logger', Mock())
@patch('evostream.commands.protocol', TestHTTPProtocol(LIST_STREAMS_IDS_TEST_DATA))
class ListStreamsIdsTestCase(TestCase):
    def test_success(self):
        ids = list_streams_ids()
        self.assertListEqual(ids, LIST_STREAMS_IDS_TEST_DATA['data'])


if django.VERSION >= (1, 5):
    @patch('evostream.commands.logger', Mock())
    @patch('evostream.commands.protocol', TestHTTPProtocol(LIST_STREAMS_IDS_TEST_DATA))
    @patch('django.core.management.base.OutputWrapper.write')
    class ListStreamsIdsCommandTestCase(TestCase):
        def test_verbose(self, mock_write):
            call_command('liststreamsids')
            self.assertEqual(mock_write.call_count, 1)
            self.assertEqual(mock_write.call_args,
                             [(json.dumps(LIST_STREAMS_IDS_TEST_DATA['data'], indent=1, sort_keys=True),)])

GET_STREAM_INFO_TEST_DATA = load_test_data('get_stream_info.json')


@patch('evostream.commands.logger', Mock())
@patch('evostream.commands.protocol', TestHTTPProtocol(GET_STREAM_INFO_TEST_DATA))
class GetStreamInfoTestCase(TestCase):
    def test_success(self):
        ids = get_stream_info(id=1)
        self.assertDictEqual(ids, GET_STREAM_INFO_TEST_DATA['data'])


if django.VERSION >= (1, 5):
    @patch('evostream.commands.logger', Mock())
    @patch('evostream.commands.protocol', TestHTTPProtocol(GET_STREAM_INFO_TEST_DATA))
    @patch('django.core.management.base.OutputWrapper.write')
    class GetStreamInfoCommandTestCase(TestCase):
        def test_verbose(self, mock_write):
            call_command('getstreaminfo', id_or_local_stream_name=1, verbosity=2)
            self.assertEqual(mock_write.call_count, 1)
            self.assertEqual(mock_write.call_args,
                             [(json.dumps(GET_STREAM_INFO_TEST_DATA['data'], indent=1, sort_keys=True),)])

        def test_silent(self, mock_write):
            call_command('getstreaminfo', id_or_local_stream_name=1)
            self.assertEqual(mock_write.call_count, 2)
            self.assertListEqual(mock_write.call_args_list,
                                 [[('uniqueId: 1\n',)],
                                  [('name: "testpullstream"\n',)]])

LIST_STREAMS_TEST_DATA = load_test_data('list_streams.json')


@patch('evostream.commands.logger', Mock())
@patch('evostream.commands.protocol', TestHTTPProtocol(LIST_STREAMS_TEST_DATA))
class ListStreamsTestCase(TestCase):
    def test_success(self):
        ids = list_streams()
        self.assertListEqual(ids, LIST_STREAMS_TEST_DATA['data'])


if django.VERSION >= (1, 5):
    @patch('evostream.commands.logger', Mock())
    @patch('evostream.commands.protocol', TestHTTPProtocol(LIST_STREAMS_TEST_DATA))
    @patch('django.core.management.base.OutputWrapper.write')
    class ListStreamsCommandTestCase(TestCase):
        def test_verbose(self, mock_write):
            call_command('liststreams', verbosity=2)
            self.assertEqual(mock_write.call_count, 1)
            self.assertEqual(mock_write.call_args,
                             [(json.dumps(LIST_STREAMS_TEST_DATA['data'], indent=1, sort_keys=True),)])

        def test_silent(self, mock_write):
            call_command('liststreams')
            self.assertEqual(mock_write.call_count, 2)
            self.assertListEqual(mock_write.call_args_list,
                                 [[('uniqueId: 36\n',)],
                                  [('name: "testpullstream"\n',)]])

GET_STREAMS_COUNT_TEST_DATA = load_test_data('get_streams_count.json')


@patch('evostream.commands.logger', Mock())
@patch('evostream.commands.protocol', TestHTTPProtocol(GET_STREAMS_COUNT_TEST_DATA))
class GetStreamsCountTestCase(TestCase):
    def test_success(self):
        cnt = get_streams_count()
        self.assertDictEqual(cnt, GET_STREAMS_COUNT_TEST_DATA['data'])


if django.VERSION >= (1, 5):
    @patch('evostream.commands.logger', Mock())
    @patch('evostream.commands.protocol', TestHTTPProtocol(GET_STREAMS_COUNT_TEST_DATA))
    @patch('django.core.management.base.OutputWrapper.write')
    class GetStreamsCountCommandTestCase(TestCase):
        def test_verbose(self, mock_write):
            call_command('getstreamscount')
            self.assertEqual(mock_write.call_count, 1)
            self.assertEqual(mock_write.call_args,
                             [(json.dumps(GET_STREAMS_COUNT_TEST_DATA['data'], indent=1, sort_keys=True),)])
