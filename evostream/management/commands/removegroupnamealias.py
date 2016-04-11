from evostream.commands import remove_group_name_alias
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    args = '<aliasName>'

    help = 'Removes an alias of a group.'

    requires_system_checks = False

    def get_results(self, alias_name, *args, **options):
        return remove_group_name_alias(aliasName=alias_name)
