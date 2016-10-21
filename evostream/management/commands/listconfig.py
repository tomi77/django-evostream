from evostream.default import api
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Returns a list with all push/pull configurations.'

    requires_system_checks = False

    def get_results(self, *args, **options):
        return api.list_config()
