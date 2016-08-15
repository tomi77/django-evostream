from optparse import make_option

import django

from evostream.commands import add_stream_alias
from evostream.management.base import BaseEvoStreamCommand


class Command(BaseEvoStreamCommand):
    help = 'Create secondary name for internal stream.'

    requires_system_checks = False

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('localStreamName', type=str,
                                help='The original stream name.')
            parser.add_argument('aliasName', type=str,
                                help='The alias alternative to the'
                                     'localStreamName.')
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
        args = '<localStreamName> <aliasName>'

        option_list = BaseEvoStreamCommand.option_list + (
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

    def get_results(self, localStreamName, aliasName, *args, **options):
        return add_stream_alias(localStreamName=localStreamName,
                                aliasName=aliasName, **options)
