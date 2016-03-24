import json

from evostream.commands import get_config_info
from evostream.management.base import EvoStreamCommand


class Command(EvoStreamCommand):
    args = '<config_id>'

    help = 'Returns the information of the stream by the configId.'

    requires_system_checks = False

    def get_results(self, config_id, *args, **options):
        return get_config_info(id=int(config_id))

    def format_results(self, results, verbosity):
        if verbosity > 1:
            super(Command, self).format_results(results, verbosity=verbosity)
        else:
            for stream in results:
                for key, val in stream.items():
                    if key in ('configId', 'localStreamName'):
                        self.stdout.write(key + ': ' + json.dumps(val) + '\n')
        self.stdout.write('\n')
