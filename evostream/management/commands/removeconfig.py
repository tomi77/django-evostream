from optparse import make_option

import django

from evostream.commands import remove_config
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    args = '<id_or_groupName>'

    help = 'Stop the stream and remove the corresponding configuration entry.'

    requires_system_checks = False

    silent_keys = 'configId',

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('--remove_hls_hds_files', action='store',
                                type=int, choices=[0, 1], default=0,
                                dest='removeHlsHdsFiles',
                                help='Remove folder associated with HLS/HDS stream')
    else:
        option_list = BaseEvoStreamCommand.option_list + (
            make_option('--remove_hls_hds_files', action='store',
                        type='choice', choices=['0', '1'], default='0',
                        dest='removeHlsHdsFiles',
                        help='Remove folder associated with HLS/HDS stream'),
        )

    def get_results(self, id_or_group_name, *args, **options):
        try:
            return remove_config(id=int(id_or_group_name), **options)
        except ValueError:
            return remove_config(groupName=id_or_group_name, **options)
