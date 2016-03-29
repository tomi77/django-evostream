from evostream.commands import get_streams_count
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Returns the number of active streams.'

    requires_system_checks = False

    def get_results(self, *args, **options):
        return get_streams_count()