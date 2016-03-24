import json
from optparse import make_option

import django

from evostream.commands import add_stream_alias
from evostream.management.base import EvoStreamCommand


class Command(EvoStreamCommand):
    args = '<local_stream_name> <alias_name>'

    help = 'Create secondary name for internal stream.'

    requires_system_checks = False

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('--expire-period', action='store',
                                type=int, default=-600,
                                dest='expirePeriod',
                                help='The expiration period for this alias. '
                                     'Negative values will be treated as '
                                     'one-shot but no longer than the '
                                     'absolute positive value in seconds, 0 '
                                     'means it will not expire, positive '
                                     'values mean the alias can be used '
                                     'multiple times but expires after this '
                                     'many seconds. The default is -600 '
                                     '(one-shot, 10 mins)')
    else:
        option_list = EvoStreamCommand.option_list + (
            make_option('--expire-period', action='store',
                        type='int', default=-600,
                        dest='expirePeriod',
                        help='The expiration period for this alias. Negative '
                             'values will be treated as one-shot but no '
                             'longer than the absolute positive value in '
                             'seconds, 0 means it will not expire, positive '
                             'values mean the alias can be used multiple '
                             'times but expires after this many seconds. The '
                             'default is -600 (one-shot, 10 mins)'),
        )

    def get_results(self, local_stream_name, alias_name, *args, **options):
        return add_stream_alias(localStreamName=local_stream_name,
                                aliasName=alias_name, **options)
