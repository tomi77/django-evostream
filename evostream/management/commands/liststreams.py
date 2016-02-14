import json

from django.core.management.base import BaseCommand

from evostream import EvoStreamException
from evostream.commands import liststreams


class Command(BaseCommand):
    requires_system_checks = False

    def handle(self, *args, **options):
        try:
            streams = liststreams()
        except EvoStreamException as ex:
            self.stderr.write(str(ex) + '\n')
            return
        if streams['data'] is None:
            self.stdout.write('No data\n')
            return
        for stream in streams['data']:
            self.stdout.write(json.dumps(stream) + '\n')
