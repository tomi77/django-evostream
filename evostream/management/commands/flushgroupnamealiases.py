from evostream.commands import flush_group_name_aliases
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Invalidates all group name aliases.'

    requires_system_checks = False

    def get_results(self, *args, **options):
        return flush_group_name_aliases()
