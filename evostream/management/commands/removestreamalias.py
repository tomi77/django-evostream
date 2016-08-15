import django

from evostream.commands import remove_stream_alias
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Removes an alias of a stream.'

    requires_system_checks = False

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('aliasName', type=str,
                                help='The alias to delete.')
    else:
        args = '<aliasName>'

    def get_results(self, aliasName, *args, **options):
        return remove_stream_alias(aliasName=aliasName)
