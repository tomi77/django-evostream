from optparse import make_option

import django

from evostream.commands import list_streams
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Provides a detailed description of all active streams.'

    requires_system_checks = False

    silent_keys = 'uniqueId', 'name'

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('--disable-internal-streams', action='store',
                                type=int, choices=[0, 1], default=0,
                                dest='disableInternalStreams',
                                help='Filtering out internal streams from the list')
    else:
        option_list = BaseEvoStreamCommand.option_list + (
            make_option('--disable-internal-streams', action='store',
                        type='choice', choices=['0', '1'], default='0',
                        dest='disableInternalStreams',
                        help='Filtering out internal streams from the list'),
        )

    def get_results(self, *args, **options):
        return list_streams(**options)
