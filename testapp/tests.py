import json

import os

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'testapp.settings'
if hasattr(django, 'setup'):
    django.setup()

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
    return json.load(open(os.path.join(os.path.dirname(__file__), 'testdata', filename)))


PULL_STREAM_TEST_DATA = load_test_data('pull_stream.json')
PUSH_STREAM_TEST_DATA = load_test_data('push_stream.json')
LIST_STREAMS_IDS_TEST_DATA = load_test_data('list_streams_ids.json')
GET_STREAM_INFO_TEST_DATA = load_test_data('get_stream_info.json')
LIST_STREAMS_TEST_DATA = load_test_data('list_streams.json')
GET_STREAMS_COUNT_TEST_DATA = load_test_data('get_streams_count.json')
SHUTDOWN_STREAM_TEST_DATA = load_test_data('shutdown_stream.json')
LIST_CONFIG_TEST_DATA = load_test_data('list_config.json')
REMOVE_CONFIG_TEST_DATA = load_test_data('remove_config.json')
GET_CONFIG_INFO_TEST_DATA = load_test_data('get_config_info.json')
ADD_STREAM_ALIAS_TEST_DATA = load_test_data('add_stream_alias.json')
LIST_STREAM_ALIASES_TEST_DATA = load_test_data('list_stream_aliases.json')
REMOVE_STREAM_ALIAS_TEST_DATA = load_test_data('remove_stream_alias.json')
FLUSH_STREAM_ALIASES_TEST_DATA = load_test_data('flush_stream_aliases.json')
ADD_GROUP_NAME_ALIAS_TEST_DATA = load_test_data('add_group_name_alias.json')
FLUSH_GROUP_NAME_ALIASES_TEST_DATA = load_test_data('flush_group_name_aliases.json')
GET_GROUP_NAME_BY_ALIAS_TEST_DATA = load_test_data('get_group_name_by_alias.json')
LIST_GROUP_NAME_ALIASES_TEST_DATA = load_test_data('list_group_name_aliases.json')
REMOVE_GROUP_NAME_ALIAS_TEST_DATA = load_test_data('remove_group_name_alias.json')
LIST_HTTP_STREAMING_SESSIONS_TEST_DATA = load_test_data('list_http_streaming_sessions.json')
CREATE_INGEST_POINT_TEST_DATA = load_test_data('create_ingest_point.json')
REMOVE_INGEST_POINT_TEST_DATA = load_test_data('remove_ingest_point.json')
LIST_INGEST_POINTS_TEST_DATA = load_test_data('list_ingest_points.json')
CREATE_HLS_STREAM_TEST_DATA = load_test_data('create_hls_stream.json')


@patch('evostream.commands.protocol', TestHTTPProtocol(PULL_STREAM_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class PullStreamTestCase(TestCase):
    def test_api(self):
        out = pull_stream(uri='rtmp://s2pchzxmtymn2k.cloudfront.net/cfx/st/mp4:sintel.mp4',
                          localStreamName='testpullstream')
        self.assertDictEqual(out, PULL_STREAM_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('pullstream', 'rtmp://s2pchzxmtymn2k.cloudfront.net/cfx/st/mp4:sintel.mp4',
                         localStreamName='testpullstream')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['localStreamName']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(PUSH_STREAM_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class PushStreamTestCase(TestCase):
    def test_api(self):
        out = push_stream(uri='rtmp://DestinationAddress/live',
                          localStreamName='testpullstream', targetStreamName='testpushStream')
        self.assertDictEqual(out, PUSH_STREAM_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('pushstream', 'rtmp://DestinationAddress/live',
                         localStreamName='testpullstream', targetStreamName='testpushStream')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['localStreamName']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(LIST_STREAMS_IDS_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class ListStreamsIdsTestCase(TestCase):
    def test_api(self):
        out = list_streams_ids()
        self.assertListEqual(out, LIST_STREAMS_IDS_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('liststreamsids')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for _id in ['205', '206', '207']:
                try:
                    out.index(_id)
                except ValueError:
                    self.fail('ID %s not found' % _id)


@patch('evostream.commands.protocol', TestHTTPProtocol(GET_STREAM_INFO_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class GetStreamInfoTestCase(TestCase):
    def test_api(self):
        out = get_stream_info(id=1)
        self.assertDictEqual(out, GET_STREAM_INFO_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('getstreaminfo', '1', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in GET_STREAM_INFO_TEST_DATA['data'].keys():
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('getstreaminfo', '1')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['uniqueId', 'name']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(LIST_STREAMS_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class ListStreamsTestCase(TestCase):
    def test_api(self):
        out = list_streams()
        self.assertListEqual(out, LIST_STREAMS_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('liststreams', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for data in LIST_STREAMS_TEST_DATA['data']:
                for key in data.keys():
                    try:
                        out.index(key)
                    except ValueError:
                        self.fail('Key %s not found' % key)

        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('liststreams')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['uniqueId', 'name']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(GET_STREAMS_COUNT_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class GetStreamsCountTestCase(TestCase):
    def test_api(self):
        out = get_streams_count()
        self.assertDictEqual(out, GET_STREAMS_COUNT_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('getstreamscount')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in GET_STREAMS_COUNT_TEST_DATA['data'].keys():
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(SHUTDOWN_STREAM_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class ShutdownStreamTestCase(TestCase):
    def test_api(self):
        out = shutdown_stream(id=55)
        self.assertDictEqual(out, SHUTDOWN_STREAM_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('shutdownstream', '55')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in SHUTDOWN_STREAM_TEST_DATA['data'].keys():
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(LIST_CONFIG_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class ListConfigTestCase(TestCase):
    def test_api(self):
        out = list_config()
        self.assertDictEqual(out, LIST_CONFIG_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('listconfig')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in LIST_CONFIG_TEST_DATA['data'].keys():
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(REMOVE_CONFIG_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class RemoveConfigTestCase(TestCase):
    def test_api(self):
        out = remove_config(id=555)
        self.assertDictEqual(out, REMOVE_CONFIG_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('removeconfig', '555', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in REMOVE_CONFIG_TEST_DATA['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('removeconfig', '555')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['configId']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(GET_CONFIG_INFO_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class GetConfigInfoTestCase(TestCase):
    def test_api(self):
        out = get_config_info(1)
        self.assertDictEqual(out, GET_CONFIG_INFO_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('getconfiginfo', '1', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in GET_CONFIG_INFO_TEST_DATA['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('getconfiginfo', '1')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['configId', 'localStreamName']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(ADD_STREAM_ALIAS_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class AddStreamAliasTestCase(TestCase):
    def test_api(self):
        out = add_stream_alias('MyStream', 'video1', expirePeriod=-300)
        self.assertDictEqual(out, ADD_STREAM_ALIAS_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('addstreamalias', 'MyStream', 'video1', expirePeriod=-300)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ADD_STREAM_ALIAS_TEST_DATA['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(LIST_STREAM_ALIASES_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class ListStreamAliasesTestCase(TestCase):
    def test_api(self):
        out = list_stream_aliases()
        self.assertListEqual(out, LIST_STREAM_ALIASES_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('liststreamaliases', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for data in LIST_STREAM_ALIASES_TEST_DATA['data']:
                for key in data:
                    try:
                        out.index(key)
                    except ValueError:
                        self.fail('Key %s not found' % key)

        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('liststreamaliases')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['aliasName', 'localStreamName']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(REMOVE_STREAM_ALIAS_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class RemoveStreamAliasTestCase(TestCase):
    def test_api(self):
        out = remove_stream_alias(aliasName='video1')
        self.assertDictEqual(out, REMOVE_STREAM_ALIAS_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('removestreamalias', 'video1')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in REMOVE_STREAM_ALIAS_TEST_DATA['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(FLUSH_STREAM_ALIASES_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class FlushStreamAliasesTestCase(TestCase):
    def test_api(self):
        out = flush_stream_aliases()
        self.assertIsNone(out)

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('flushstreamaliases')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            try:
                out.index('No data')
            except ValueError:
                self.fail('Key "No data" not found')


@patch('evostream.commands.protocol', TestHTTPProtocol(ADD_GROUP_NAME_ALIAS_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class AddGroupNameAliasTestCase(TestCase):
    def test_api(self):
        out = add_group_name_alias(groupName='MyGroup', aliasName='TestGroupAlias')
        self.assertDictEqual(out, ADD_GROUP_NAME_ALIAS_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('addgroupnamealias', 'MyGroup', 'TestGroupAlias', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ADD_GROUP_NAME_ALIAS_TEST_DATA['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('addgroupnamealias', 'MyGroup', 'TestGroupAlias')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['aliasName', 'groupName']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(FLUSH_GROUP_NAME_ALIASES_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class FlushGroupNameAliasesTestCase(TestCase):
    def test_api(self):
        out = flush_stream_aliases()
        self.assertIsNone(out)

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('flushgroupnamealiases')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            try:
                out.index('No data')
            except ValueError:
                self.fail('Key "No data" not found')


@patch('evostream.commands.protocol', TestHTTPProtocol(GET_GROUP_NAME_BY_ALIAS_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class GetGroupNameByAliasTestCase(TestCase):
    def test_api(self):
        out = get_group_name_by_alias(aliasName='TestGroupAlias')
        self.assertDictEqual(out, GET_GROUP_NAME_BY_ALIAS_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('getgroupnamebyalias', 'TestGroupAlias', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in GET_GROUP_NAME_BY_ALIAS_TEST_DATA['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('getgroupnamebyalias', 'TestGroupAlias')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['aliasName', 'groupName']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(LIST_GROUP_NAME_ALIASES_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class ListGroupNameAliasesTestCase(TestCase):
    def test_api(self):
        out = list_group_name_aliases()
        self.assertListEqual(out, LIST_GROUP_NAME_ALIASES_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('listgroupnamealiases')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for data in LIST_GROUP_NAME_ALIASES_TEST_DATA['data']:
                for key in data:
                    try:
                        out.index(key)
                    except ValueError:
                        self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(REMOVE_GROUP_NAME_ALIAS_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class RemoveGroupNameAliasTestCase(TestCase):
    def test_api(self):
        out = remove_group_name_alias(aliasName='TestGroupAlias')
        self.assertDictEqual(out, REMOVE_GROUP_NAME_ALIAS_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('removegroupnamealias', 'video1')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in REMOVE_GROUP_NAME_ALIAS_TEST_DATA['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(LIST_HTTP_STREAMING_SESSIONS_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class ListHttpStreamingSessionsTestCase(TestCase):
    def test_api(self):
        out = list_http_streaming_sessions()
        self.assertListEqual(out, LIST_HTTP_STREAMING_SESSIONS_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('listhttpstreamingsessions')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for data in LIST_HTTP_STREAMING_SESSIONS_TEST_DATA['data']:
                for key in data:
                    try:
                        out.index(key)
                    except ValueError:
                        self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(CREATE_INGEST_POINT_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class CreateIngestPointTestCase(TestCase):
    def test_api(self):
        out = create_ingest_point(privateStreamName='theIngestPoint', publicStreamName='useMeToViewStream')
        self.assertDictEqual(out, CREATE_INGEST_POINT_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('createingestpoint', 'theIngestPoint', 'useMeToViewStream')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in CREATE_INGEST_POINT_TEST_DATA['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(REMOVE_INGEST_POINT_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class RemoveIngestPointTestCase(TestCase):
    def test_api(self):
        out = remove_ingest_point(privateStreamName='theIngestPoint')
        self.assertDictEqual(out, REMOVE_INGEST_POINT_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('removeingestpoint', 'theIngestPoint')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in REMOVE_INGEST_POINT_TEST_DATA['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(LIST_INGEST_POINTS_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class ListIngestPointsTestCase(TestCase):
    def test_api(self):
        out = list_ingest_points()
        self.assertListEqual(out, LIST_INGEST_POINTS_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('listingestpoints')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for data in LIST_INGEST_POINTS_TEST_DATA['data']:
                for key in data:
                    try:
                        out.index(key)
                    except ValueError:
                        self.fail('Key %s not found' % key)


@patch('evostream.commands.protocol', TestHTTPProtocol(CREATE_HLS_STREAM_TEST_DATA))
@patch('evostream.commands.logger', Mock())
class CreateHLSStreamTestCase(TestCase):
    def test_api(self):
        out = create_hls_stream('hlstest', '/MyWebRoot/', bandwidths=128, groupName='hls',
                                playlistType='rolling', playlistLength=10, chunkLength=5)
        self.assertDictEqual(out, CREATE_HLS_STREAM_TEST_DATA['data'])

    if django.VERSION >= (1, 5):
        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('createhlsstream', 'hlstest', '/MyWebRoot/', bandwidths=128, groupName='hls',
                         playlistType='rolling', playlistLength=10, chunkLength=5, verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in CREATE_HLS_STREAM_TEST_DATA['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('createhlsstream', 'hlstest', '/MyWebRoot/', bandwidths=128, groupName='hls',
                         playlistType='rolling', playlistLength=10, chunkLength=5)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['localStreamNames', 'targetFolder']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)
