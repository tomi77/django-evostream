from evostream.commands import get_streams_count
from evostream.management.base import EvoStreamCommand


class Command(EvoStreamCommand):
    help = 'Returns the number of active streams.'

    requires_system_checks = False

    def get_results(self, **options):
        return get_streams_count()
