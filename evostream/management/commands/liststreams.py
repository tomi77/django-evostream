import json
from optparse import make_option

import django
from django.core.management.base import BaseCommand

from evostream import EvoStreamException
from evostream.commands import list_streams


class Command(BaseCommand):
    help = 'Provides a detailed description of all active streams.'

    requires_system_checks = False

    if django.VERSION[:2] > (1, 7):
        def add_arguments(self, parser):
            parser.add_argument('--disable-internal-streams', action='store',
                                type=int, choices=[0, 1], default=0,
                                dest='disableInternalStreams',
                                help='Filtering out internal streams from the list')
    else:
        option_list = BaseCommand.option_list + (
            make_option('--disable-internal-streams', action='store',
                        type='choice', choices=['0', '1'], default='0',
                        dest='disableInternalStreams',
                        help='Filtering out internal streams from the list'),
        )

    def handle(self, verbosity, *args, **options):
        try:
            streams = list_streams(**options)
        except EvoStreamException as ex:
            self.stderr.write(str(ex) + '\n')
            return
        if streams is None:
            self.stdout.write('No data\n')
            return
        for stream in streams:
            for key in stream.keys():
                if verbosity > 1 or key in ('uniqueId', 'name'):
                    self.stdout.write(key + ': ' + json.dumps(stream[key]) + '\n')
            self.stdout.write('\n')
