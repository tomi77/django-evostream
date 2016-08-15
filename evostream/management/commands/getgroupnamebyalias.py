import django

from evostream.commands import get_group_name_by_alias
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Returns the group name given the alias name.'

    requires_system_checks = False

    silent_keys = ['aliasName', 'groupName']

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('aliasName', type=str,
                                help='The group alias name.')
    else:
        args = '<aliasName>'

    def get_results(self, aliasName, *args, **options):
        return get_group_name_by_alias(aliasName=aliasName)
