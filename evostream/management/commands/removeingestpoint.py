from evostream.commands import remove_ingest_point
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    args = '<privateStreamName>'

    help = 'Removes an RTMP ingest point.'

    requires_system_checks = False

    def get_results(self, private_stream_name, *args, **options):
        return remove_ingest_point(privateStreamName=private_stream_name)
