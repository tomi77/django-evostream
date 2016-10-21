from evostream.default import api
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Returns a lists the currently available Ingest Points.'

    requires_system_checks = False

    def get_results(self, *args, **options):
        return api.list_ingest_points()
