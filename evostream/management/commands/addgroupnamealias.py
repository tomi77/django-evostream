from evostream.commands import add_group_name_alias
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    args = '<groupName> <aliasName>'

    help = 'Create secondary name for group name.'

    requires_system_checks = False

    silent_keys = ['aliasName', 'groupName']

    def get_results(self, group_name, alias_name, *args, **options):
        return add_group_name_alias(groupName=group_name, aliasName=alias_name)
