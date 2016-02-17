import json
from optparse import make_option

import django

from evostream.commands import list_streams
from evostream.management.base import EvoStreamCommand


class Command(EvoStreamCommand):
    help = 'Provides a detailed description of all active streams.'

    requires_system_checks = False

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('--disable-internal-streams', action='store',
                                type=int, choices=[0, 1], default=0,
                                dest='disableInternalStreams',
                                help='Filtering out internal streams from the list')
    else:
        option_list = EvoStreamCommand.option_list + (
            make_option('--disable-internal-streams', action='store',
                        type='choice', choices=['0', '1'], default='0',
                        dest='disableInternalStreams',
                        help='Filtering out internal streams from the list'),
        )

    def get_results(self, **options):
        return list_streams(**options)

    def format_results(self, results, verbosity):
        if verbosity > 1:
            super(Command, self).format_results(results, verbosity=verbosity)
        else:
            for stream in results:
                for key, val in stream.items():
                    if key in ('uniqueId', 'name'):
                        self.stdout.write(key + ': ' + json.dumps(val) + '\n')
        self.stdout.write('\n')
