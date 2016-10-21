import json
import os

import django
from pyems.protocols import HTTPProtocol

from evostream.default import api

os.environ['DJANGO_SETTINGS_MODULE'] = 'testapp.settings'
if hasattr(django, 'setup'):
    django.setup()

try:
    from unittest import mock
except ImportError:
    import mock

from django.core.management import call_command
from django.test import TestCase


class TestHTTPProtocol(HTTPProtocol):
    def __init__(self, result):
        self.result = json.dumps(result)

    def get_result(self, command, **params):
        return self.result


def load_test_data(filename):
    fh = open(os.path.join(os.path.dirname(__file__), 'testdata', filename), 'r')
    data = json.load(fh)
    fh.close()
    return data


class EmsTestCase(TestCase):
    data_file = None
    data = None

    def setUp(self):
        self.data = load_test_data(self.data_file)
        api.protocol = TestHTTPProtocol(self.data)


@mock.patch('pyems.utils.logger', mock.Mock())
class PullStreamTestCase(EmsTestCase):
    data_file = 'pull_stream.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
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


@mock.patch('pyems.utils.logger', mock.Mock())
class PushStreamTestCase(EmsTestCase):
    data_file = 'push_stream.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
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


@mock.patch('pyems.utils.logger', mock.Mock())
class ListStreamsIdsTestCase(EmsTestCase):
    data_file = 'list_streams_ids.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('liststreamsids')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for _id in ['205', '206', '207']:
                try:
                    out.index(_id)
                except ValueError:
                    self.fail('ID %s not found' % _id)


@mock.patch('pyems.utils.logger', mock.Mock())
class GetStreamInfoTestCase(EmsTestCase):
    data_file = 'get_stream_info.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('getstreaminfo', '1', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data'].keys():
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('getstreaminfo', '1')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['uniqueId', 'name']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class ListStreamsTestCase(EmsTestCase):
    data_file = 'list_streams.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('liststreams', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for data in self.data['data']:
                for key in data.keys():
                    try:
                        out.index(key)
                    except ValueError:
                        self.fail('Key %s not found' % key)

        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('liststreams')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['uniqueId', 'name']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class GetStreamsCountTestCase(EmsTestCase):
    data_file = 'get_streams_count.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('getstreamscount')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data'].keys():
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class ShutdownStreamTestCase(EmsTestCase):
    data_file = 'shutdown_stream.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('shutdownstream', '55')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data'].keys():
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class ListConfigTestCase(EmsTestCase):
    data_file = 'list_config.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('listconfig')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data'].keys():
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class RemoveConfigTestCase(EmsTestCase):
    data_file = 'remove_config.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('removeconfig', '555', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('removeconfig', '555')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['configId']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class GetConfigInfoTestCase(EmsTestCase):
    data_file = 'get_config_info.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('getconfiginfo', '1', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('getconfiginfo', '1')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['configId', 'localStreamName']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class AddStreamAliasTestCase(EmsTestCase):
    data_file = 'add_stream_alias.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('addstreamalias', 'MyStream', 'video1', expirePeriod=-300)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class ListStreamAliasesTestCase(EmsTestCase):
    data_file = 'list_stream_aliases.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('liststreamaliases', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for data in self.data['data']:
                for key in data:
                    try:
                        out.index(key)
                    except ValueError:
                        self.fail('Key %s not found' % key)

        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('liststreamaliases')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['aliasName', 'localStreamName']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class RemoveStreamAliasTestCase(EmsTestCase):
    data_file = 'remove_stream_alias.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('removestreamalias', 'video1')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class FlushStreamAliasesTestCase(EmsTestCase):
    data_file = 'flush_stream_aliases.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('flushstreamaliases')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            try:
                out.index('No data')
            except ValueError:
                self.fail('Key "No data" not found')


@mock.patch('pyems.utils.logger', mock.Mock())
class AddGroupNameAliasTestCase(EmsTestCase):
    data_file = 'add_group_name_alias.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('addgroupnamealias', 'MyGroup', 'TestGroupAlias', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('addgroupnamealias', 'MyGroup', 'TestGroupAlias')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['aliasName', 'groupName']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class FlushGroupNameAliasesTestCase(EmsTestCase):
    data_file = 'flush_group_name_aliases.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('flushgroupnamealiases')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            try:
                out.index('No data')
            except ValueError:
                self.fail('Key "No data" not found')


@mock.patch('pyems.utils.logger', mock.Mock())
class GetGroupNameByAliasTestCase(EmsTestCase):
    data_file = 'get_group_name_by_alias.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('getgroupnamebyalias', 'TestGroupAlias', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('getgroupnamebyalias', 'TestGroupAlias')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['aliasName', 'groupName']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class ListGroupNameAliasesTestCase(EmsTestCase):
    data_file = 'list_group_name_aliases.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('listgroupnamealiases')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for data in self.data['data']:
                for key in data:
                    try:
                        out.index(key)
                    except ValueError:
                        self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class RemoveGroupNameAliasTestCase(EmsTestCase):
    data_file = 'remove_group_name_alias.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('removegroupnamealias', 'video1')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class ListHttpStreamingSessionsTestCase(EmsTestCase):
    data_file = 'list_http_streaming_sessions.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('listhttpstreamingsessions')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for data in self.data['data']:
                for key in data:
                    try:
                        out.index(key)
                    except ValueError:
                        self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class CreateIngestPointTestCase(EmsTestCase):
    data_file = 'create_ingest_point.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('createingestpoint', 'theIngestPoint', 'useMeToViewStream')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class RemoveIngestPointTestCase(EmsTestCase):
    data_file = 'remove_ingest_point.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('removeingestpoint', 'theIngestPoint')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class ListIngestPointsTestCase(EmsTestCase):
    data_file = 'list_ingest_points.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('listingestpoints')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for data in self.data['data']:
                for key in data:
                    try:
                        out.index(key)
                    except ValueError:
                        self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class CreateHLSStreamTestCase(EmsTestCase):
    data_file = 'create_hls_stream.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('createhlsstream', 'hlstest', '/MyWebRoot/', bandwidths=128, groupName='hls',
                         playlistType='rolling', playlistLength=10, chunkLength=5, verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @mock.patch('django.core.management.base.OutputWrapper.write')
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


@mock.patch('pyems.utils.logger', mock.Mock())
class CreateHDSStreamTestCase(EmsTestCase):
    data_file = 'create_hds_stream.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('createhdsstream', 'testpullStream', '../evo-webroot', groupName='hds',
                         playlistType='rolling', verbosity=2)
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)

        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli(self, mock_write):
            call_command('createhdsstream', 'testpullStream', '../evo-webroot', groupName='hds',
                         playlistType='rolling')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in ['localStreamNames', 'targetFolder']:
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)


@mock.patch('pyems.utils.logger', mock.Mock())
class IsStreamRunningTestCase(EmsTestCase):
    data_file = 'is_stream_running.json'

    if django.VERSION >= (1, 5):
        @mock.patch('django.core.management.base.OutputWrapper.write')
        def test_cli_verbose(self, mock_write):
            call_command('isstreamrunning', '1')
            self.assertGreaterEqual(mock_write.call_count, 1)
            out = ''.join([z for x in mock_write.call_args_list for y in x for z in y])
            for key in self.data['data'].keys():
                try:
                    out.index(key)
                except ValueError:
                    self.fail('Key %s not found' % key)
