from evostream.commands import list_streams_ids
from evostream.management.base import EvoStreamCommand


class Command(EvoStreamCommand):
    help = 'Get a list of IDs for every active stream.'

    requires_system_checks = False

    def get_results(self, **options):
        return list_streams_ids()
