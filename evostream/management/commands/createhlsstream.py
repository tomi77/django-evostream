from optparse import make_option

import django

from evostream.commands import create_hls_stream
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Create an HTTP Live Stream (HLS) out of an existing H.264/AAC' \
           'stream.'

    requires_system_checks = False

    silent_keys = ('localStreamNames', 'targetFolder')

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('localStreamNames', type=str,
                                help='The stream(s) that will be used as the '
                                     'input. This is a comma-delimited list '
                                     'of active stream names (local stream '
                                     'names).')
            parser.add_argument('targetFolder', type=str,
                                help='The folder where all the .ts/.m3u8 '
                                     'files will be stored. This folder must '
                                     'be accessible by the HLS clients. It is '
                                     'usually in the web-root of the server.')
            parser.add_argument('--keep-alive', action='store',
                                type=int, choices=[0, 1], default=1,
                                dest='keepAlive',
                                help='If true, the EMS will attempt to '
                                     'reconnect to the stream source if the '
                                     'connection is severed.')
            parser.add_argument('--overwrite-destination', action='store',
                                type=int, choices=[0, 1], default=1,
                                dest='overwriteDestination',
                                help='If true, it will force overwrite of '
                                     'destination files.')
            parser.add_argument('--stale-retention-count', action='store',
                                type=int,
                                dest='staleRetentionCount',
                                help='The number of old files kept besides '
                                     'the ones listed in the current version '
                                     'of the playlist (only rolling '
                                     'playlist).')
            parser.add_argument('--create-master-playlist', action='store',
                                type=int, choices=[0, 1], default=1,
                                dest='createMasterPlaylist',
                                help='If true, a master playlist will be '
                                     'created.')
            parser.add_argument('--cleanup-destination', action='store',
                                type=int, choices=[0, 1], default=0,
                                dest='cleanupDestination',
                                help='If true, all *.ts and *.m3u8 files in '
                                     'the target folder will be removed '
                                     'before HLS creation is started.')
            parser.add_argument('--bandwidths', action='store', type=str,
                                dest='bandwidths',
                                help='The corresponding bandwidths for each '
                                     'stream listed in localStreamNames. '
                                     'Again, this can be a comma-delimited '
                                     'list.')
            parser.add_argument('--groupName', action='store', type=str,
                                dest='groupName',
                                help='The name assigned to the HLS stream or '
                                     'group.')
            parser.add_argument('--playlist-type', action='store',
                                type=str, choices=['appending', 'rolling'],
                                default='appending', dest='playlistType')
            parser.add_argument('--playlist-length', action='store',
                                type=int, default=10, dest='playlistLength',
                                help='The length (number of elements) of the '
                                     'playlist (only rolling playlist).')
            parser.add_argument('--playlist-name', action='store',
                                type=str, default='playlist.m3u8',
                                dest='playlistName',
                                help='The file name of the playlist (*.m3u8).')
            parser.add_argument('--chunk-length', action='store',
                                type=int, default=10, dest='chunkLength',
                                help='The length (in seconds) of each '
                                     'playlist element (*.ts file). Minimum '
                                     'value is 1 (second).')
            parser.add_argument('--max-chunk-length', action='store',
                                type=int, default=0, dest='maxChunkLength',
                                help='Maximum length (in seconds) the EMS '
                                     'will allow any single chunk to be.')
            parser.add_argument('--chunk-base-name', action='store',
                                type=str, dest='chunkBaseName',
                                help='The base name used to generate the *.ts '
                                     'chunks.')
            parser.add_argument('--chunk-on-idr', action='store',
                                type=int, choices=[0, 1], default=1,
                                dest='chunkOnIDR',
                                help='If true, chunking is performed ONLY on '
                                     'IDR. Otherwise, chunking is performed '
                                     'whenever chunk length is achieved.')
            parser.add_argument('--drm-type', action='store',
                                type=str, choices=['none', 'evo',
                                                   'SAMPLE-AES', 'verimatrix'],
                                default='none', dest='drmType',
                                help='Type of DRM encryption to use.')
            parser.add_argument('--aes-key-count', action='store',
                                type=int, default=5, dest='AESKeyCount',
                                help='Number of keys that will be '
                                     'automatically generated and rotated '
                                     'over while encrypting this HLS stream.')
            parser.add_argument('--audio-only', action='store',
                                type=int, choices=[0, 1], default=0,
                                dest='audioOnly',
                                help='If true, stream will be audio only.')
            parser.add_argument('--hls-resume', action='store',
                                type=int, choices=[0, 1], default=0,
                                dest='hlsResume',
                                help='If true, HLS will resume in appending '
                                     'segments to previously created child '
                                     'playlist even in cases of EMS shutdown '
                                     'or cut off stream source.')
            parser.add_argument('--cleanup-on-close', action='store',
                                type=int, choices=[0, 1], default=0,
                                dest='cleanupOnClose',
                                help='If true, corresponding hls files to a '
                                     'stream will be deleted if the said '
                                     'stream is removed or shut down or '
                                     'disconnected.')
            parser.add_argument('--use-byte-range', action='store',
                                type=int, choices=[0, 1], default=0,
                                dest='useByteRange',
                                help='If true, will use the EXT-X-BYTERANGE '
                                     'feature of HLS (version 4 and up).')
            parser.add_argument('--file-length', action='store',
                                type=int, dest='fileLength',
                                help='When using useByteRange=1, this '
                                     'parameter needs to be set too. This '
                                     'will be the size of file before '
                                     'chunking it to another file, this '
                                     'replace the chunkLength in case of '
                                     'EXT-X-BYTERANGE, since chunkLength will '
                                     'be the byte range chunk.')
            parser.add_argument('--use-system-time', action='store',
                                type=int, choices=[0, 1], default=0,
                                dest='useSystemTime',
                                help='If true, uses UTC in playlist time '
                                     'stamp otherwise will use the local '
                                     'server time.')
            parser.add_argument('--offset-time', action='store',
                                type=int, default=0, dest='offsetTime')
            parser.add_argument('--start-offset', action='store',
                                type=int, default=0, dest='startOffset',
                                help='A parameter valid only for HLS v.6 '
                                     'onwards. This will indicate the start '
                                     'offset time (in seconds) for the '
                                     'playback of the playlist.')
    else:
        args = '<localStreamNames> <targetFolder>'

        option_list = BaseEvoStreamCommand.option_list + (
            make_option('--keep-alive', action='store',
                        type='choice', choices=['0', '1'], default='1',
                        dest='keepAlive',
                        help='If true, the EMS will attempt to reconnect to '
                             'the stream source if the connection is '
                             'severed.'),
            make_option('--overwrite-destination', action='store',
                        type='choice', choices=['0', '1'], default='1',
                        dest='overwriteDestination',
                        help='If true, it will force overwrite of destination '
                             'files.'),
            make_option('--stale-retention-count', action='store',
                        type='int',
                        dest='staleRetentionCount',
                        help='The number of old files kept besides the ones '
                             'listed in the current version of the playlist '
                             '(only rolling playlist).'),
            make_option('--create-master-playlist', action='store',
                        type='choice', choices=['0', '1'], default='1',
                        dest='createMasterPlaylist',
                        help='If true, a master playlist will be created.'),
            make_option('--cleanup-destination', action='store',
                        type='choice', choices=['0', '1'], default='0',
                        dest='cleanupDestination',
                        help='If true, all *.ts and *.m3u8 files in the '
                             'target folder will be removed before HLS '
                             'creation is started.'),
            make_option('--bandwidths', action='store', type='string',
                        dest='bandwidths',
                        help='The corresponding bandwidths for each stream '
                             'listed in localStreamNames. Again, this can be '
                             'a comma-delimited list.'),
            make_option('--groupName', action='store', type='string',
                        dest='groupName',
                        help='The name assigned to the HLS stream or group.'),
            make_option('--playlist-type', action='store',
                        type='choice', choices=['appending', 'rolling'],
                        default='appending', dest='playlistType'),
            make_option('--playlist-length', action='store',
                        type='int', default=10, dest='playlistLength',
                        help='The length (number of elements) of the playlist '
                             '(only rolling playlist).'),
            make_option('--playlist-name', action='store',
                        type='string', default='playlist.m3u8',
                        dest='playlistName',
                        help='The file name of the playlist (*.m3u8).'),
            make_option('--chunk-length', action='store',
                        type='int', default=10, dest='chunkLength',
                        help='The length (in seconds) of each playlist '
                             'element (*.ts file). Minimum value is 1 '
                             '(second).'),
            make_option('--max-chunk-length', action='store',
                        type='int', default=0, dest='maxChunkLength',
                        help='Maximum length (in seconds) the EMS will allow '
                             'any single chunk to be.'),
            make_option('--chunk-base-name', action='store',
                        type='string', dest='chunkBaseName',
                        help='The base name used to generate the *.ts '
                             'chunks.'),
            make_option('--chunk-on-idr', action='store',
                        type='choice', choices=['0', '1'], default='1',
                        dest='chunkOnIDR',
                        help='If true, chunking is performed ONLY on IDR. '
                             'Otherwise, chunking is performed whenever chunk '
                             'length is achieved.'),
            make_option('--drm-type', action='store',
                        type='choice', choices=['none', 'evo', 'SAMPLE-AES',
                                                'verimatrix'],
                        default='none', dest='drmType',
                        help='Type of DRM encryption to use.'),
            make_option('--aes-key-count', action='store',
                        type='int', default=5, dest='AESKeyCount',
                        help='Number of keys that will be automatically '
                             'generated and rotated over while encrypting '
                             'this HLS stream.'),
            make_option('--audio-only', action='store',
                        type='choice', choices=['0', '1'], default='0',
                        dest='audioOnly',
                        help='If true, stream will be audio only.'),
            make_option('--hls-resume', action='store',
                        type='choice', choices=['0', '1'], default='0',
                        dest='hlsResume',
                        help='If true, HLS will resume in appending segments '
                             'to previously created child playlist even in '
                             'cases of EMS shutdown or cut off stream '
                             'source.'),
            make_option('--cleanup-on-close', action='store',
                        type='choice', choices=['0', '1'], default='0',
                        dest='cleanupOnClose',
                        help='If true, corresponding hls files to a stream '
                             'will be deleted if the said stream is removed '
                             'or shut down or disconnected.'),
            make_option('--use-byte-range', action='store',
                        type='choice', choices=['0', '1'], default='0',
                        dest='useByteRange',
                        help='If true, will use the EXT-X-BYTERANGE feature '
                             'of HLS (version 4 and up).'),
            make_option('--file-length', action='store',
                        type='int', dest='fileLength',
                        help='When using --use-byte-range=1, this parameter '
                             'needs to be set too. This will be the size of '
                             'file before chunking it to another file, this '
                             'replace the chunkLength in case of '
                             'EXT-X-BYTERANGE, since chunkLength will be the '
                             'byte range chunk.'),
            make_option('--use-system-time', action='store',
                        type='choice', choices=['0', '1'], default='0',
                        dest='useSystemTime',
                        help='If true, uses UTC in playlist time stamp '
                             'otherwise will use the local server time.'),
            make_option('--offset-time', action='store',
                        type='int', default='0', dest='offsetTime'),
            make_option('--start-offset', action='store',
                        type='int', default='0', dest='startOffset',
                        help='A parameter valid only for HLS v.6 onwards. '
                             'This will indicate the start offset time (in '
                             'seconds) for the playback of the playlist.'),
        )

    def get_results(self, localStreamNames, targetFolder, *args, **options):
        return create_hls_stream(localStreamNames=localStreamNames,
                                 targetFolder=targetFolder, **options)
