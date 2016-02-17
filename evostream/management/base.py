import json

from django.core.management.base import BaseCommand

from evostream import EvoStreamException


class EvoStreamCommand(BaseCommand):
    requires_system_checks = False

    def get_results(self, **options):
        raise NotImplementedError()

    def format_results(self, results, verbosity):
        self.stdout.write(json.dumps(results, indent=1, sort_keys=True))

    def handle(self, verbosity, *args, **options):
        try:
            results = self.get_results(**options)
        except EvoStreamException as ex:
            self.stderr.write(str(ex) + '\n')
            return
        if results is None:
            self.stdout.write('No data\n')
            return
        self.format_results(results, verbosity=verbosity)
