from evostream.commands import remove_stream_alias
from evostream.management.base import EvoStreamCommand


class Command(EvoStreamCommand):
    args = '<aliasName>'

    help = 'Removes an alias of a stream.'

    requires_system_checks = False

    def get_results(self, aliasName, *args, **options):
        return remove_stream_alias(aliasName)
