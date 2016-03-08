from django import get_version


VERSION = (0, 2, 0, 'beta', 1)
__author__ = "Tomasz Jakub Rup"
__email__ = "tomasz.rup@gmail.com"
__version__ = get_version(VERSION)
__license__ = "MIT"


class EvoStreamException(Exception):
    pass
