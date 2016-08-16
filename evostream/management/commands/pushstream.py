from optparse import make_option

import django

from evostream.commands import push_stream
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Push a local stream to an external destination.'

    requires_system_checks = False

    silent_keys = ('localStreamName',)

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('uri', type=str,
                                help='The URI of the external stream. Can be '
                                     'RTMP, RTSP or unicast/multicast (d) '
                                     'mpegts.')
            parser.add_argument('--keep-alive', action='store',
                                type=int, choices=[0, 1], default=1,
                                dest='keepAlive',
                                help='If keepAlive is set to 1, the server '
                                     'will attempt to reestablish connection '
                                     'with a stream source after a connection '
                                     'has been lost. The reconnect will be '
                                     'attempted once every second.')
            parser.add_argument('--local-stream-name', action='store',
                                type=str, dest='localStreamName',
                                help='Name of the stream. Otherwise, a '
                                     'fallback techniques used to determine '
                                     'the stream name (based on the URI).')
            parser.add_argument('--force-tcp', action='store',
                                type=int, choices=[0, 1], default=1,
                                dest='forceTcp',
                                help='If 1 and if the stream is RTSP, a TCP '
                                     'connection will be forced. Otherwise '
                                     'the transport mechanism will be '
                                     'negotiated (UDP or TCP).')
            parser.add_argument('--tc-url', action='store',
                                type=str, dest='tcUrl',
                                help='TC URL to use in the initial RTMP '
                                     'connect invoke.')
            parser.add_argument('--page-url', action='store',
                                type=str, dest='pageUrl',
                                help='Originating web page address to use in '
                                     'the initial RTMP connect invoke.')
            parser.add_argument('--swf-url', action='store',
                                type=str, dest='swfUrl',
                                help='Originating swf URL to use in the '
                                     'initial RTMP connect invoke.')
            parser.add_argument('--range-start', action='store',
                                type=int, dest='rangeStart',
                                help='A value from which the playback should '
                                     'start expressed in seconds '
                                     '(RTSP and RTMP connections only).')
            parser.add_argument('--range-end', action='store',
                                type=int, dest='rangeEnd',
                                help='The length in seconds for the playback '
                                     '(RTSP and RTMP connections only).')
            parser.add_argument('--ttl', action='store',
                                type=int, dest='ttl',
                                help='Sets the IP_TTL (time to live) option '
                                     'on the socket.')
            parser.add_argument('--tos', action='store',
                                type=int, dest='tos',
                                help='Sets the IP_TOS (Type of Service) '
                                     'option on the socket.')
            parser.add_argument('--rtcp-detection-interval', action='store',
                                type=int, dest='rtcpDetectionInterval',
                                help='How much time (in seconds) should the '
                                     'server wait for RTCP packets before '
                                     'declaring the RTSP stream as a '
                                     'RTCP-less stream.')
            parser.add_argument('--emulate-user-agent', action='store',
                                type=str, dest='emulateUserAgent',
                                help='User agent string (only for RTMP).')
            parser.add_argument('--is-audio', action='store',
                                type=int, choices=[0, 1], dest='isAudio',
                                help='If 1 and if the stream is RTP, it '
                                     'indicates that the currently pulled '
                                     'stream is an audio source. Otherwise '
                                     'the pulled source is assumed as a '
                                     'video source.')
            parser.add_argument('--audio-codec-bytes', action='store',
                                type=str, dest='audioCodecBytes',
                                help='The audio codec setup of RTP stream if '
                                     'it is audio. Represented as hex format '
                                     'without "0x" or "h".')
            parser.add_argument('--sps-bytes', action='store',
                                type=str, dest='spsBytes',
                                help='The video SPS bytes of RTP stream if '
                                     'it is video. It should be base 64 '
                                     'encoded.')
            parser.add_argument('--pps-bytes', action='store',
                                type=str, dest='ppsBytes',
                                help='The video PPS bytes of RTP stream if '
                                     'it is video. It should be base 64 '
                                     'encoded.')
            parser.add_argument('--ssm-ip', action='store',
                                type=str, dest='ssmIp',
                                help='The source IP from source-specific-'
                                     'multicast (only UDP based pull).')
            parser.add_argument('--http-proxy', action='store',
                                type=str, dest='httpProxy',
                                help='IP:Port - specifies an RTSP HTTP Proxy '
                                     'from which the RTSP stream should be '
                                     'pulled; "self" - pulling RTSP over '
                                     'HTTP.')
    else:
        args = '<uri>'

        option_list = BaseEvoStreamCommand.option_list + (
            make_option('--keep-alive', action='store',
                        type='choice', choices=['0', '1'], default='1',
                        dest='keepAlive',
                        help='If keepAlive is set to 1, the server will '
                             'attempt to reestablish connection with a stream '
                             'source after a connection has been lost. The '
                             'reconnect will be attempted once every second.'),
            make_option('--local-stream-name', action='store', type='string',
                        dest='localStreamName',
                        help='Name of the stream. Otherwise, a fallback '
                             'techniques used to determine the stream name '
                             '(based on the URI).'),
            make_option('--force-tcp', action='store',
                        type='choice', choices=['0', '1'], default='1',
                        dest='forceTcp',
                        help='If 1 and if the stream is RTSP, a TCP '
                             'connection will be forced. Otherwise the '
                             'transport mechanism will be negotiated '
                             '(UDP or TCP).'),
            make_option('--tc-url', action='store', type='string',
                        dest='tcUrl',
                        help='TC URL to use in the initial RTMP connect '
                             'invoke.'),
            make_option('--page-url', action='store', type='string',
                        dest='pageUrl',
                        help='Originating web page address to use in the '
                             'initial RTMP connect invoke.'),
            make_option('--swf-url', action='store', type='string',
                        dest='swfUrl',
                        help='Originating swf URL to use in the initial RTMP '
                             'connect invoke.'),
            make_option('--range-start', action='store', type='int',
                        dest='rangeStart',
                        help='A value from which the playback should start '
                             'expressed in seconds '
                             '(RTSP and RTMP connections only).'),
            make_option('--range-end', action='store', type='int',
                        dest='rangeEnd',
                        help='The length in seconds for the playback '
                             '(RTSP and RTMP connections only).'),
            make_option('--ttl', action='store', type='int', dest='ttl',
                        help='Sets the IP_TTL (time to live) option on the '
                             'socket.'),
            make_option('--tos', action='store', type='int', dest='tos',
                        help='Sets the IP_TOS (Type of Service) option on '
                             'the socket.'),
            make_option('--rtcp-detection-interval', action='store',
                        type='int', dest='rtcpDetectionInterval',
                        help='How much time (in seconds) should the server '
                             'wait for RTCP packets before declaring the '
                             'RTSP stream as a RTCP-less stream.'),
            make_option('--emulate-user-agent', action='store',
                        type='string', dest='emulateUserAgent',
                        help='User agent string (only for RTMP).'),
            make_option('--is-audio', action='store',
                        type='choice', choices=['0', '1'],
                        dest='isAudio',
                        help='If 1 and if the stream is RTP, it indicates '
                             'that the currently pulled stream is an audio '
                             'source. Otherwise the pulled source is assumed '
                             'as a video source.'),
            make_option('--audio-codec-bytes', action='store',
                        type='string', dest='audioCodecBytes',
                        help='The audio codec setup of RTP stream if it is '
                             'audio. Represented as hex format without '
                             '"0x" or "h".'),
            make_option('--sps-bytes', action='store',
                        type='string', dest='spsBytes',
                        help='The video SPS bytes of RTP stream if it is '
                             'video. It should be base 64 encoded.'),
            make_option('--pps-bytes', action='store',
                        type='string', dest='ppsBytes',
                        help='The video PPS bytes of RTP stream if it is '
                             'video. It should be base 64 encoded.'),
            make_option('--ssm-ip', action='store',
                        type='string', dest='ssmIp',
                        help='The source IP from source-specific-multicast '
                             '(only UDP based pull).'),
            make_option('--http-proxy', action='store',
                        type='string', dest='httpProxy',
                        help='IP:Port - specifies an RTSP HTTP Proxy from '
                             'which the RTSP stream should be pulled; "self" '
                             '- pulling RTSP over HTTP.'),
        )

    def get_results(self, uri, *args, **options):
        return push_stream(uri=uri, **options)
