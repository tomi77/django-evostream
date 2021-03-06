from evostream.default import api
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Get a list of IDs for every active stream.'

    requires_system_checks = False

    def get_results(self, *args, **options):
        return api.list_streams_ids()
