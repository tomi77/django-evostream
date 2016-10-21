from evostream.default import api
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Invalidates all streams aliases.'

    requires_system_checks = False

    def get_results(self, *args, **options):
        return api.flush_stream_aliases()
