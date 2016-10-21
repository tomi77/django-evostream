from evostream.default import api
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Returns a complete list of group name aliases.'

    requires_system_checks = False

    def get_results(self, *args, **options):
        return api.list_group_name_aliases()
