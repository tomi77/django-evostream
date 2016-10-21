import django

from evostream.default import api
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Removes an alias of a group.'

    requires_system_checks = False

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('aliasName', type=str,
                                help='The alias alternative to be removed '
                                     'from the group name.')
    else:
        args = '<aliasName>'

    def get_results(self, aliasName, *args, **options):
        return api.remove_group_name_alias(aliasName=aliasName)
