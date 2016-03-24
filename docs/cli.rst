.. _ref-cli:

============
Command Line
============

``addstreamalias``
==================

Allows you to create secondary name(s) for internal streams. Once an alias is
created the localstreamname cannot be used to request playback of that stream.
Once an alias is used (requested by a client) the alias is removed. Aliases
are designed to be used to protect/hide your source streams.

Example:
::

    ./manage.py addstreamalias bunny video1 --expire-period=-300

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

``liststreamaliases``
=====================

Returns a complete list of aliases.

Example
::

    ./manage.py liststreamaliases

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

``removestreamalias``
=====================

Removes an alias of a stream.

Example
::

    ./manage.py removestreamalias video1
