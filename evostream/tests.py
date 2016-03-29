import json

import django

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

from django.core.management import call_command
from django.test import TestCase
from evostream import EvoStreamException
from evostream.commands import list_streams_ids, list_streams
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


LIST_STREAMS_TEST_DATA = {
    "data": [
        {
            "appName": "evostreamms",
            "audio": {
                "bytesCount": 727893,
                "codec": "AAAC",
                "codecNumeric": 4702111241970122752,
                "droppedBytesCount": 0,
                "droppedPacketsCount": 0,
                "packetsCount": 2243
            },
            "bandwidth": 0,
            "connectionType": 1,
            "creationTimestamp": 1448005740350.4519,
            "edgePid": 0,
            "farIp": "54.239.131.224",
            "farPort": 1935,
            "ip": "192.168. 2.35",
            "name": "testpullstream",
            "nearIp": "192.168.2.35",
            "nearPort": 1607,
            "outStream sUniqueIds": None,
            "pageUrl": "",
            "port": 1607,
            "processId": 12848,
            "processType": "origin",
            "pullSettings": {
                "_callback": None,
                "audioCodecBytes": "",
                "configId": 1,
                "emulateUs erAgent": "EvoStream Media Server (www.evostream.com) player",
                "forceTcp": False,
                "httpProxy": "",
                "isAudio": True,
                "keepAlive": True,
                "localStreamName": "testpullstream",
                "operationType": 1,
                "pageUrl": "",
                "ppsBytes": "",
                "rangeEnd": -1,
                "rangeStart": -2,
                "rtcp DetectionInterval": 10,
                "sendRenewStream": False,
                "spsBytes": "",
                "ssmIp": "",
                "swfUrl": "",
                "tcUrl": "",
                "tos": 256,
                "ttl": 256,
                "uri": "rtmp:\/\/s2pchzxmtymn2k.cloudfront.net\ /cfx\/st\/mp4:sintel.mp4"
            },
            "queryTimestamp": 1448005784755.9919,
            "serverAgent": "FMS\/3,5,7,7009",
            "swfUrl": "rtmp:\/\/s2pchzxmtymn2k.cloudfront.net\/cfx\/st\/mp4:sintel.mp4",
            "tcUrl": "rtmp:\/\/s2pchzxmtymn2k.cloudfront.net\/cfx\/st\/mp4:sintel.mp4",
            "type": "INR",
            "typeNumeric": 5282249572905648128,
            "uniqueId": 36,
            "upTime": 44405.5400,
            "video": {
                "bytesCount": 4881934,
                "codec": "VH264",
                "codecNumeric": 6217274493967007744,
                "droppedBytesCount": 0,
                "droppedPacketsCount": 0,
                "height": 306,
                "level": 30,
                "packetsCount": 1255,
                "profile": 66,
                "width": 720
            }
        }
    ],
    "description": "Available streams",
    "status": "SUCCESS"
}


@patch('evostream.commands.logger', Mock())
class ListStreamsTestCase(TestCase):
    @patch('evostream.commands.protocol', TestProtocol(json.dumps(LIST_STREAMS_TEST_DATA)))
    def test_success(self):
        ids = list_streams()
        self.assertListEqual(ids, LIST_STREAMS_TEST_DATA['data'])


if django.VERSION >= (1, 5):
    @patch('evostream.commands.logger', Mock())
    class ListStreamsCommandTestCase(TestCase):
        @patch('evostream.commands.protocol', TestProtocol(json.dumps(LIST_STREAMS_TEST_DATA)))
        @patch('django.core.management.base.OutputWrapper.write')
        def test_verbose(self, mock_write):
            call_command('liststreams', verbosity=2)
            self.assertEqual(mock_write.call_count, 1)
            self.assertEqual(mock_write.call_args,
                             [(json.dumps(LIST_STREAMS_TEST_DATA['data'], indent=1, sort_keys=True),)])

        @patch('evostream.commands.protocol', TestProtocol(json.dumps(LIST_STREAMS_TEST_DATA)))
        @patch('django.core.management.base.OutputWrapper.write')
        def test_silent(self, mock_write):
            call_command('liststreams')
            self.assertEqual(mock_write.call_count, 2)
            self.assertListEqual(mock_write.call_args_list,
                                 [[('uniqueId: 36\n',)],
                                  [('name: "testpullstream"\n',)]])


LIST_STREAMS_IDS_TEST_DATA = {
    "data": [205, 206, 207],
    "description": "Available stream IDs",
    "status": "SUCCESS"
}


@patch('evostream.commands.logger', Mock())
class ListStreamsIdsTestCase(TestCase):
    @patch('evostream.commands.protocol', TestProtocol(json.dumps(LIST_STREAMS_IDS_TEST_DATA)))
    def test_success(self):
        ids = list_streams_ids()
        self.assertListEqual(ids, LIST_STREAMS_IDS_TEST_DATA['data'])


if django.VERSION >= (1, 5):
    @patch('evostream.commands.logger', Mock())
    class ListStreamsIdsCommandTestCase(TestCase):
        @patch('evostream.commands.protocol', TestProtocol(json.dumps(LIST_STREAMS_IDS_TEST_DATA)))
        @patch('django.core.management.base.OutputWrapper.write')
        def test_verbose(self, mock_write):
            call_command('liststreamsids')
            self.assertEqual(mock_write.call_count, 1)
            self.assertEqual(mock_write.call_args,
                             [(json.dumps(LIST_STREAMS_IDS_TEST_DATA['data'], indent=1, sort_keys=True),)])
