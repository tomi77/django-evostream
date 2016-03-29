from evostream.commands import flush_stream_aliases
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Invalidates all streams aliases.'

    requires_system_checks = False

    def get_results(self, *args, **options):
        return flush_stream_aliases()
