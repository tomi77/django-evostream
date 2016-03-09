.. _ref-cli:

============
Command Line
============

``getstreamscount``
===================

Returns the number of active streams.

Example
::

    ./manage.py getstreamscount

``liststreamsids``
==================

Get a list of IDs for every active stream.

Example
::

    ./manage.py liststreamsids

``listconfig``
==============

Returns a list with all push/pull configurations.

Example
::

    ./manage.py listconfig

``liststreams``
===============

Provides a detailed description of all active streams.

Parameters:

* ``--disable-internal-streams`` Filtering out internal streams from the list.

Example
::

    ./manage.py liststreams --disable-internal-streams=1

