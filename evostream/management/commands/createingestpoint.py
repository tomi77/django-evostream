from evostream.commands import create_ingest_point
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    args = '<privateStreamName> <publicStreamName>'

    help = 'Creates an RTMP ingest point.'

    requires_system_checks = False

    def get_results(self, private_stream_name, public_stream_name,
                    *args, **options):
        return create_ingest_point(privateStreamName=private_stream_name,
                                   publicStreamName=public_stream_name,
                                   **options)
