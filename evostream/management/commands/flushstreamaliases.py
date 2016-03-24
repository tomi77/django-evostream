from evostream.commands import flush_stream_aliases
from evostream.management.base import EvoStreamCommand


class Command(EvoStreamCommand):
    help = 'Invalidates all streams aliases.'

    requires_system_checks = False

    def get_results(self, *args, **options):
        return flush_stream_aliases()
