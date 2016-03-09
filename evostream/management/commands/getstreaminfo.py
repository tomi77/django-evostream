import json

from evostream.commands import get_stream_info
from evostream.management.base import EvoStreamCommand


class Command(EvoStreamCommand):
    args = '<id_or_localStreamName>'

    help = 'Returns a detailed set of information about a stream.'

    requires_system_checks = False

    def get_results(self, id_or_local_stream_name, *args, **options):
        try:
            return get_stream_info(id=int(id_or_local_stream_name))
        except ValueError:
            return get_stream_info(localStreamName=id_or_local_stream_name)

    def format_results(self, results, verbosity):
        if verbosity > 1:
            super(Command, self).format_results(results, verbosity=verbosity)
        else:
            for stream in results:
                for key, val in stream.items():
                    if key in ('uniqueId', 'name'):
                        self.stdout.write(key + ': ' + json.dumps(val) + '\n')
        self.stdout.write('\n')
