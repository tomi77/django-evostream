from evostream.commands import get_stream_info
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    args = '<id_or_localStreamName>'

    help = 'Returns a detailed set of information about a stream.'

    requires_system_checks = False

    silent_keys = ('uniqueId', 'name')

    def get_results(self, id_or_local_stream_name, *args, **options):
        try:
            return get_stream_info(id=int(id_or_local_stream_name))
        except ValueError:
            return get_stream_info(localStreamName=id_or_local_stream_name)
