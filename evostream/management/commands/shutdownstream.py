from optparse import make_option

import django

from evostream.default import api
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Returns a detailed set of information about a stream.'

    requires_system_checks = False

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('idOrLocalStreamName', type=str,
                                help='The uniqueId of the stream or the name '
                                     'of the inbound stream that needs to be '
                                     'terminated.')
            parser.add_argument('--permanently', action='store',
                                type=int, choices=[0, 1], default=0,
                                dest='permanently',
                                help='Terminate push/pull configuration')
    else:
        args = '<idOrLocalStreamName>'

        option_list = BaseEvoStreamCommand.option_list + (
            make_option('--permanently', action='store',
                        type='choice', choices=['0', '1'], default='0',
                        dest='permanently',
                        help='Terminate push/pull configuration'),
        )

    def get_results(self, idOrLocalStreamName, *args, **options):
        try:
            return api.shutdown_stream(id=int(idOrLocalStreamName), **options)
        except ValueError:
            return api.shutdown_stream(localStreamName=idOrLocalStreamName,
                                       **options)
