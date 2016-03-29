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
            if not isinstance(results, list):
                results = [results]
            for result in results:
                for key in self.silent_keys:
                    if key in result:
                        self.stdout.write(key + ': ' + json.dumps(result[key]) + '\n')

    def handle(self, verbosity, *args, **options):
        if not isinstance(verbosity, int):
            verbosity = int(verbosity)

        try:
            results = self.get_results(*args, **options)
        except EvoStreamException as ex:
            self.stderr.write(str(ex) + '\n')
            return

        if results is None:
            self.stdout.write('No data\n')
            return

        self.format_results(results, verbosity=verbosity)
