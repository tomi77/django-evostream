from optparse import make_option

import django

from evostream.default import api
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Create an HDS (HTTP Dynamic Streaming) stream out of an ' \
           'existing H.264/AAC stream.'

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
            parser.add_argument('--bandwidths', action='store', type=str,
                                dest='bandwidths',
                                help='The corresponding bandwidths for each '
                                     'stream listed in localStreamNames. '
                                     'Again, this can be a comma-delimited '
                                     'list.')
            parser.add_argument('--chunk-base-name', action='store',
                                type=str, dest='chunkBaseName',
                                help='The base name used to generate the'
                                     'fragments.')
            parser.add_argument('--chunk-length', action='store',
                                type=int, default=10, dest='chunkLength',
                                help='The length (in seconds) of fragments to '
                                     'be made. Minimum value is 1 (second).')
            parser.add_argument('--chunk-on-idr', action='store',
                                type=int, choices=[0, 1], default=1,
                                dest='chunkOnIDR',
                                help='If true, chunking is performed ONLY on '
                                     'IDR. Otherwise, chunking is performed '
                                     'whenever chunk length is achieved.')
            parser.add_argument('--groupName', action='store', type=str,
                                dest='groupName',
                                help='The name assigned to the HDS stream or '
                                     'group.')
            parser.add_argument('--keep-alive', action='store',
                                type=int, choices=[0, 1], default=1,
                                dest='keepAlive',
                                help='If true, the EMS will attempt to '
                                     'reconnect to the stream source if the '
                                     'connection is severed.')
            parser.add_argument('--manifest-name', action='store', type=str,
                                dest='manifestName',
                                help='The manifest file name.')
            parser.add_argument('--overwrite-destination', action='store',
                                type=int, choices=[0, 1], default=1,
                                dest='overwriteDestination',
                                help='If true, it will allow overwrite of '
                                     'destination files.')
            parser.add_argument('--playlist-type', action='store',
                                type=str, choices=['appending', 'rolling'],
                                default='appending', dest='playlistType')
            parser.add_argument('--playlist-length', action='store',
                                type=int, default=10, dest='playlistLength',
                                help='The number of fragments before the '
                                     'server starts to overwrite the older '
                                     'fragments (only rolling playlist).')
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
                                help='If true, all manifest and fragment '
                                     'files in the target folder will be '
                                     'removed before HDS creation is started.')
    else:
        args = '<localStreamNames> <targetFolder>'

        option_list = BaseEvoStreamCommand.option_list + (
            make_option('--bandwidths', action='store', type='string',
                        dest='bandwidths',
                        help='The corresponding bandwidths for each stream '
                             'listed in localStreamNames. Again, this can be '
                             'a comma-delimited list.'),
            make_option('--chunk-base-name', action='store',
                        type='string', dest='chunkBaseName',
                        help='The base name used to generate the fragments.'),
            make_option('--chunk-length', action='store',
                        type='int', default=10, dest='chunkLength',
                        help='The length (in seconds) of fragments to be '
                             'made. Minimum value is 1 (second).'),
            make_option('--chunk-on-idr', action='store',
                        type='choice', choices=['0', '1'], default='1',
                        dest='chunkOnIDR',
                        help='If true, chunking is performed ONLY on IDR. '
                             'Otherwise, chunking is performed whenever chunk '
                             'length is achieved.'),
            make_option('--groupName', action='store', type='string',
                        dest='groupName',
                        help='The name assigned to the HDS stream or group.'),
            make_option('--keep-alive', action='store',
                        type='choice', choices=['0', '1'], default='1',
                        dest='keepAlive',
                        help='If true, the EMS will attempt to reconnect to '
                             'the stream source if the connection is '
                             'severed.'),
            make_option('--manifest-name', action='store', type='string',
                        dest='manifestName',
                        help='The manifest file name.'),
            make_option('--overwrite-destination', action='store',
                        type='choice', choices=['0', '1'], default='1',
                        dest='overwriteDestination',
                        help='If true, it will allow overwrite of destination '
                             'files.'),
            make_option('--playlist-type', action='store',
                        type='choice', choices=['appending', 'rolling'],
                        default='appending', dest='playlistType'),
            make_option('--playlist-length', action='store',
                        type='int', default=10, dest='playlistLength',
                        help='The number of fragments before the server '
                             'starts to overwrite the older fragments '
                             '(only rolling playlist).'),
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
                        help='If true, all manifest and fragment files in the '
                             'target folder will be removed before HDS '
                             'creation is started.'),
        )

    def get_results(self, localStreamNames, targetFolder, *args, **options):
        return api.create_hls_stream(localStreamNames=localStreamNames,
                                     targetFolder=targetFolder, **options)
