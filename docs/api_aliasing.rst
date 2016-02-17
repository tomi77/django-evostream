.. _ref-api_aliasing:

========
Aliasing
========

``get_stream_info``
===================

Returns a detailed set of information about a stream.

Required:

One of these parameters is required.

:``id`` `(int)`:
    The uniqueId of the stream. Usually a value returned by listStreamsIDs.

:``localStreamName`` `(str)`:
    The name of the stream.

Example::

 get_stream_info(id=1)

http://docs.evostream.com/ems_api_definition/getstreaminfo

``list_streams``
================

Provides a detailed description of all active streams.

Optional:

:``disableInternalStreams`` `(int)`:
    If this is 1 (true), internal streams (origin-edge related) are filtered
    out from the list

Example::

 list_streams()

http://docs.evostream.com/ems_api_definition/liststreams

``shutdown_stream``
===================

Terminates a specific stream. When ``permanently=1`` is used, this command is
analogous to ``remove_config``.

Required:

One of these parameters is required.

:``id`` `(int)`:
    The uniqueId of the stream that needs to be terminated. The
    stream ID’s can be obtained using the listStreams command.

:``localStreamName`` `(str)`:
    The name of the inbound stream which you wish to
    terminate. This will also terminate any outbound streams that are
    dependent upon this input stream.

Optional:

:``permanently`` `(int)`:
    If true, the corresponding push/pull configuration will
    also be terminated. Therefore, the stream will NOT be reconnected when
    the server restarts

Example::

 shutdown_stream(id=55)

http://docs.evostream.com/ems_api_definition/shutdownstream

``list_config``
===============

Returns a list with all push/pull configurations.

Whenever the pullStream or pushStream interfaces are called, a record
containing the details of the pull or push is created in the
``pullpushconfig.xml`` file. Then, the next time the EMS is started, the
``pullpushconfig.xml`` file is read, and the EMS attempts to reconnect all of
the previous pulled or pushed streams.

Example::

 list_config()

http://docs.evostream.com/ems_api_definition/listconfig

``remove_config``
=================

This command will both stop the stream and remove the corresponding
configuration entry. This command is the same as performing::

 shutdownStream permanently=1

Required:

One of these parameters is required.

:``id`` `(int)`:
    The configId of the configuration that needs to be removed.
    ConfigId’s can be obtained from the listConfig interface. Removing an
    inbound stream will also automatically remove all associated outbound
    streams.

:``groupName`` `(str)`:
    The name of the group that needs to be removed (applicable to HLS, HDS and
    external processes).

Optional:

:``removeHlsHdsFiles`` `(int)`:
    If 1 (true) and the stream is HLS or HDS, the folder associated with it
    will be removed.

Example::

 remove_config(id=55)

http://docs.evostream.com/ems_api_definition/removeconfig
