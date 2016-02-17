from evostream.commands import list_config
from evostream.management.base import EvoStreamCommand


class Command(EvoStreamCommand):
    help = 'Returns a list with all push/pull configurations.'

    requires_system_checks = False

    def get_results(self, **options):
        return list_config()
