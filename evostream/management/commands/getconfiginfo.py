import django

from evostream.commands import get_config_info
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Returns the information of the stream by the configId.'

    requires_system_checks = False

    silent_keys = ('configId', 'localStreamName')

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('configId', type=int,
                                help='The configId of the configuration to '
                                     'get some information.')
    else:
        args = '<configId>'

    def get_results(self, configId, *args, **options):
        return get_config_info(id=int(configId))
