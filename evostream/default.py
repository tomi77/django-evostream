from django.utils.functional import LazyObject
from pyems import Api as PyEmsApi

from .conf import settings


class Api(LazyObject):
    def _setup(self):
        self._wrapped = PyEmsApi(settings.EVOSTREAM_URI)

api = Api()
