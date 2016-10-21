from evostream.default import api
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Returns a complete list of aliases.'

    requires_system_checks = False

    silent_keys = ('aliasName', 'localStreamName')

    def get_results(self, *args, **options):
        return api.list_stream_aliases()
