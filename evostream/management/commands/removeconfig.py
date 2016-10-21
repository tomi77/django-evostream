from optparse import make_option

import django

from evostream.default import api
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Stop the stream and remove the corresponding configuration entry.'

    requires_system_checks = False

    silent_keys = 'configId',

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('idOrGroupName', type=str,
                                help='The configId of the configuration that '
                                     'needs to be removed or the name of the '
                                     'group that needs to be removed.')
            parser.add_argument('--remove_hls_hds_files', action='store',
                                type=int, choices=[0, 1], default=0,
                                dest='removeHlsHdsFiles',
                                help='Remove folder associated with HLS/HDS '
                                     'stream')
    else:
        args = '<idOrGroupName>'

        option_list = BaseEvoStreamCommand.option_list + (
            make_option('--remove_hls_hds_files', action='store',
                        type='choice', choices=['0', '1'], default='0',
                        dest='removeHlsHdsFiles',
                        help='Remove folder associated with HLS/HDS stream'),
        )

    def get_results(self, idOrGroupName, *args, **options):
        try:
            return api.remove_config(id=int(idOrGroupName), **options)
        except ValueError:
            return api.remove_config(groupName=idOrGroupName, **options)
