from evostream.commands import list_stream_aliases
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Returns a complete list of aliases.'

    requires_system_checks = False

    silent_keys = ('aliasName', 'localStreamName')

    def get_results(self, *args, **options):
        return list_stream_aliases()
