import json

from django.core.management.base import BaseCommand

from evostream import EvoStreamException


class BaseEvoStreamCommand(BaseCommand):
    requires_system_checks = False

    silent_keys = ()

    def get_results(self, *args, **options):
        raise NotImplementedError()

    def format_results(self, results, verbosity):
        if verbosity > 1 or len(self.silent_keys) == 0:
            self.stdout.write(json.dumps(results, indent=1, sort_keys=True))
        else:
            for stream in results:
                for key, val in stream.items():
                    if key in self.silent_keys:
                        self.stdout.write(key + ': ' + json.dumps(val) + '\n')

    def handle(self, verbosity, *args, **options):
        try:
            results = self.get_results(*args, **options)
        except EvoStreamException as ex:
            self.stderr.write(str(ex) + '\n')
            return
        if results is None:
            self.stdout.write('No data\n')
            return
        self.format_results(results, verbosity=verbosity)
