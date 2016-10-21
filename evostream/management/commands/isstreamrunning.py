import django

from evostream.default import api
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Checks a specific stream if it is running or not.'

    requires_system_checks = False

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('idOrLocalStreamName', type=str,
                                help='The uniqueId of the stream or the name '
                                     'of the stream.')
    else:
        args = '<idOrLocalStreamName>'

    def get_results(self, idOrLocalStreamName, *args, **options):
        try:
            return api.is_stream_running(id=int(idOrLocalStreamName))
        except ValueError:
            return api.is_stream_running(localStreamName=idOrLocalStreamName)
