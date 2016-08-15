import django

from evostream.commands import create_ingest_point
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Creates an RTMP ingest point.'

    requires_system_checks = False

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('privateStreamName', type=str,
                                help='The name that RTMP Target Stream Names '
                                     'must match.')
            parser.add_argument('publicStreamName', type=str,
                                help='The name that is used to access the '
                                     'stream pushed to the privateStreamName. '
                                     'The publicStreamName becomes the '
                                     'streams localStreamName.')
    else:
        args = '<privateStreamName> <publicStreamName>'

    def get_results(self, privateStreamName, publicStreamName,
                    *args, **options):
        return create_ingest_point(privateStreamName=privateStreamName,
                                   publicStreamName=publicStreamName,
                                   **options)
