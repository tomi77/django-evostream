from evostream.commands import list_ingest_points
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Returns a lists the currently available Ingest Points.'

    requires_system_checks = False

    def get_results(self, *args, **options):
        return list_ingest_points()
