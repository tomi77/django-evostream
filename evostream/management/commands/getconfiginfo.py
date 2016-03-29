from evostream.commands import get_config_info
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    args = '<config_id>'

    help = 'Returns the information of the stream by the configId.'

    requires_system_checks = False

    silent_keys = ('configId', 'localStreamName')

    def get_results(self, config_id, *args, **options):
        return get_config_info(id=int(config_id))
