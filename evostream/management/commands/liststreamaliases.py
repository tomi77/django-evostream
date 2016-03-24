import json

from evostream.commands import list_stream_aliases
from evostream.management.base import EvoStreamCommand


class Command(EvoStreamCommand):
    help = 'Returns a complete list of aliases.'

    requires_system_checks = False

    def get_results(self, *args, **options):
        return list_stream_aliases()

    def format_results(self, results, verbosity):
        if verbosity > 1:
            super(Command, self).format_results(results, verbosity=verbosity)
        else:
            for stream in results:
                for key, val in stream.items():
                    if key in ('aliasName', 'localStreamName'):
                        self.stdout.write(key + ': ' + json.dumps(val) + '\n')
        self.stdout.write('\n')
