import json
from optparse import make_option

from django.core.management.base import BaseCommand

from evostream import EvoStreamException
from evostream.commands import list_streams


class Command(BaseCommand):
    help = 'Provides a detailed description of all active streams.'

    requires_system_checks = False

    option_list = BaseCommand.option_list + (
        make_option('--disable-internal-streams', action='store',
                    type='choice', choices=['0', '1'], default='0',
                    help='Filtered out internal streams from the list'),
    )

    def handle(self, *args, **options):
        try:
            streams = list_streams(**options)
        except EvoStreamException as ex:
            self.stderr.write(str(ex) + '\n')
            return
        if streams['data'] is None:
            self.stdout.write('No data\n')
            return
        for stream in streams['data']:
            for key in stream.keys():
                self.stdout.write(key + ': ' + json.dumps(stream[key]) + '\n')
            self.stdout.write('\n')
