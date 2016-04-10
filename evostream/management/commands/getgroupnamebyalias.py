from evostream.commands import get_group_name_by_alias
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    args = '<aliasName>'

    help = 'Returns the group name given the alias name.'

    requires_system_checks = False

    silent_keys = ['aliasName', 'groupName']

    def get_results(self, alias_name, *args, **options):
        return get_group_name_by_alias(aliasName=alias_name)
