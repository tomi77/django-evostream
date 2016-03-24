.. _ref-cli:

============
Command Line
============

``getconfiginfo``
=================

Returns the information of the stream by the configId.

Example
::

    ./manage.py getconfiginfo 1

``getstreaminfo``
=================

Returns a detailed set of information about a stream.

Example
::

    ./manage.py getstreaminfo 1
    ./manage.py getstreaminfo streamname

``getstreamscount``
===================

Returns the number of active streams.

Example
::

    ./manage.py getstreamscount

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

``liststreamsids``
==================

Get a list of IDs for every active stream.

Example
::

    ./manage.py liststreamsids
