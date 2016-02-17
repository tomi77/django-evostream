.. _ref-cli:

============
Command Line
============

``liststreams``
===============

Provides a detailed description of all active streams.

Parameters:

* ``--disable-internal-streams`` Filtering out internal streams from the list.

Example::

 ./manage.py liststreams --disable-internal-streams=1

``listconfig``
==============

Returns a list with all push/pull configurations.

Example::

 ./manage.py listconfig
