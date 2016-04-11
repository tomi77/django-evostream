from evostream.commands import list_group_name_aliases
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Returns a complete list of group name aliases.'

    requires_system_checks = False

    def get_results(self, *args, **options):
        return list_group_name_aliases()
