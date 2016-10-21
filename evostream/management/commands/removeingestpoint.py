import django

from evostream.default import api
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Removes an RTMP ingest point.'

    requires_system_checks = False

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('privateStreamName', type=str,
                                help='The Ingest Point is identified by the '
                                     'privateStreamName, so only that is '
                                     'required to delete it.')
    else:
        args = '<privateStreamName>'

    def get_results(self, privateStreamName, *args, **options):
        return api.remove_ingest_point(privateStreamName=privateStreamName)
