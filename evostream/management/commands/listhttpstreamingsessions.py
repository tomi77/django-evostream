from evostream.commands import list_http_streaming_sessions
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Lists all currently active HTTP streaming sessions.'

    requires_system_checks = False

    def get_results(self, *args, **options):
        return list_http_streaming_sessions()
