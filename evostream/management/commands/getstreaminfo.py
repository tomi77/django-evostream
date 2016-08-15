import django

from evostream.commands import get_stream_info
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Returns a detailed set of information about a stream.'

    requires_system_checks = False

    silent_keys = ('uniqueId', 'name')

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('idOrLocalStreamName', type=str,
                                help='The uniqueId of the stream or the name '
                                     'of the stream.')
    else:
        args = '<idOrLocalStreamName>'

    def get_results(self, idOrLocalStreamName, *args, **options):
        try:
            return get_stream_info(id=int(idOrLocalStreamName))
        except ValueError:
            return get_stream_info(localStreamName=idOrLocalStreamName)
