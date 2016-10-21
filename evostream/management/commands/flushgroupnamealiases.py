from evostream.default import api
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Invalidates all group name aliases.'

    requires_system_checks = False

    def get_results(self, *args, **options):
        return api.flush_group_name_aliases()
