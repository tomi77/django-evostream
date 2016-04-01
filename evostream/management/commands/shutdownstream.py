from optparse import make_option

import django

from evostream.commands import shutdown_stream
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    args = '<id_or_localStreamName>'

    help = 'Returns a detailed set of information about a stream.'

    requires_system_checks = False

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('--permanently', action='store',
                                type=int, choices=[0, 1], default=0,
                                dest='permanently',
                                help='Terminate push/pull configuration')
    else:
        option_list = BaseEvoStreamCommand.option_list + (
            make_option('--permanently', action='store',
                        type='choice', choices=['0', '1'], default='0',
                        dest='permanently',
                        help='Terminate push/pull configuration'),
        )

    def get_results(self, id_or_local_stream_name, *args, **options):
        try:
            return shutdown_stream(id=int(id_or_local_stream_name), **options)
        except ValueError:
            return shutdown_stream(localStreamName=id_or_local_stream_name, **options)
