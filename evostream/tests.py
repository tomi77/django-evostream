import json

import os

import django

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

from django.core.management import call_command
from django.test import TestCase
from evostream.commands import *
from evostream.protocols import HTTPProtocol


class TestHTTPProtocol(HTTPProtocol):
    def __init__(self, result):
        self.result = json.dumps(result)

    def get_result(self, command, **params):
        return self.result


def load_test_data(filename):
    return json.load(open(os.path.join('testapp', 'testdata', filename)))


LIST_STREAMS_IDS_TEST_DATA = load_test_data('list_streams_ids.json')
GET_STREAM_INFO_TEST_DATA = load_test_data('get_stream_info.json')
LIST_STREAMS_TEST_DATA = load_test_data('list_streams.json')
GET_STREAMS_COUNT_TEST_DATA = load_test_data('get_streams_count.json')
SHUTDOWN_STREAM_TEST_DATA = load_test_data('shutdown_stream.json')
LIST_CONFIG_TEST_DATA = load_test_data('list_config.json')
REMOVE_CONFIG_TEST_DATA = load_test_data('remove_config.json')


@patch('evostream.commands.logger', Mock())
class ApiTestCase(TestCase):
    @patch('evostream.commands.protocol', TestHTTPProtocol(LIST_STREAMS_IDS_TEST_DATA))
    def test_list_streams_ids(self):
        out = list_streams_ids()
        self.assertListEqual(out, LIST_STREAMS_IDS_TEST_DATA['data'])

    @patch('evostream.commands.protocol', TestHTTPProtocol(GET_STREAM_INFO_TEST_DATA))
    def test_get_stream_info(self):
        out = get_stream_info(id=1)
        self.assertDictEqual(out, GET_STREAM_INFO_TEST_DATA['data'])

    @patch('evostream.commands.protocol', TestHTTPProtocol(LIST_STREAMS_TEST_DATA))
    def test_list_streams(self):
        out = list_streams()
        self.assertListEqual(out, LIST_STREAMS_TEST_DATA['data'])

    @patch('evostream.commands.protocol', TestHTTPProtocol(GET_STREAMS_COUNT_TEST_DATA))
    def test_get_streams_count(self):
        out = get_streams_count()
        self.assertDictEqual(out, GET_STREAMS_COUNT_TEST_DATA['data'])

    @patch('evostream.commands.protocol', TestHTTPProtocol(SHUTDOWN_STREAM_TEST_DATA))
    def test_shutdown_stream(self):
        out = shutdown_stream(id=55)
        self.assertDictEqual(out, SHUTDOWN_STREAM_TEST_DATA['data'])

    @patch('evostream.commands.protocol', TestHTTPProtocol(LIST_CONFIG_TEST_DATA))
    def test_list_config(self):
        out = list_config()
        self.assertDictEqual(out, LIST_CONFIG_TEST_DATA['data'])

    @patch('evostream.commands.protocol', TestHTTPProtocol(REMOVE_CONFIG_TEST_DATA))
    def test_remove_config(self):
        out = remove_config(id=555)
        self.assertDictEqual(out, REMOVE_CONFIG_TEST_DATA['data'])


if django.VERSION >= (1, 5):
    @patch('evostream.commands.logger', Mock())
    @patch('django.core.management.base.OutputWrapper.write')
    class CliTestCase(TestCase):
        @patch('evostream.commands.protocol', TestHTTPProtocol(LIST_STREAMS_IDS_TEST_DATA))
        def test_liststreamsids(self, mock_write):
            call_command('liststreamsids')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for _id in ['205', '206', '207']:
                try:
                    out.index(_id)
                except ValueError:
                    self.fail('ID %s not found' % _id)

        @patch('evostream.commands.protocol', TestHTTPProtocol(GET_STREAM_INFO_TEST_DATA))
        def test_getstreaminfo_verbose(self, mock_write):
            call_command('getstreaminfo', id_or_local_stream_name=1, verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in GET_STREAM_INFO_TEST_DATA['data'].keys():
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @patch('evostream.commands.protocol', TestHTTPProtocol(GET_STREAM_INFO_TEST_DATA))
        def test_getstreaminfo(self, mock_write):
            call_command('getstreaminfo', id_or_local_stream_name=1)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['uniqueId', 'name']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @patch('evostream.commands.protocol', TestHTTPProtocol(LIST_STREAMS_TEST_DATA))
        def test_liststreams_verbose(self, mock_write):
            call_command('liststreams', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for data in LIST_STREAMS_TEST_DATA['data']:
                for key in data.keys():
                    try:
                        out.index(key)
                    except ValueError:
                        self.fail('Key %s not found' % key)

        @patch('evostream.commands.protocol', TestHTTPProtocol(LIST_STREAMS_TEST_DATA))
        def test_liststreams(self, mock_write):
            call_command('liststreams')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['uniqueId', 'name']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @patch('evostream.commands.protocol', TestHTTPProtocol(GET_STREAMS_COUNT_TEST_DATA))
        def test_getstreamscount(self, mock_write):
            call_command('getstreamscount')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in GET_STREAMS_COUNT_TEST_DATA['data'].keys():
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @patch('evostream.commands.protocol', TestHTTPProtocol(SHUTDOWN_STREAM_TEST_DATA))
        def test_shutdownstream(self, mock_write):
            call_command('shutdownstream', id_or_local_stream_name=55)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in SHUTDOWN_STREAM_TEST_DATA['data'].keys():
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @patch('evostream.commands.protocol', TestHTTPProtocol(LIST_CONFIG_TEST_DATA))
        def test_listconfig(self, mock_write):
            call_command('listconfig')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in LIST_CONFIG_TEST_DATA['data'].keys():
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @patch('evostream.commands.protocol', TestHTTPProtocol(REMOVE_CONFIG_TEST_DATA))
        def test_liststreams_verbose(self, mock_write):
            call_command('removeconfig', id_or_group_name=555, verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in REMOVE_CONFIG_TEST_DATA['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @patch('evostream.commands.protocol', TestHTTPProtocol(REMOVE_CONFIG_TEST_DATA))
        def test_liststreams(self, mock_write):
            call_command('removeconfig', id_or_group_name=555)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['configId']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)
