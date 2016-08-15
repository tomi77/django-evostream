import django

from evostream.commands import add_group_name_alias
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Create secondary name for group name.'

    requires_system_checks = False

    silent_keys = ['aliasName', 'groupName']

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('groupName', type=str,
                                help='The original group name.')
            parser.add_argument('aliasName', type=str,
                                help='The alias alternative to the group '
                                     'name.')
    else:
        args = '<groupName> <aliasName>'

    def get_results(self, groupName, aliasName, *args, **options):
        return add_group_name_alias(groupName=groupName, aliasName=aliasName)
