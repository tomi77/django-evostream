.. _ref-cli:

============
Command Line
============

``addgroupnamealias``
=====================

This command creates secondary name(s) for group names. Once an alias is
created the group name cannot be used to request HTTP playback of that stream.
Once an alias is used (requested by a client) the alias is removed. Aliases
are designed to be used to protect/hide your source streams.

Arguments:

* ``groupName`` The original group name.

* ``aliasName`` The alias alternative to the group name.

Example:
::

    ./manage.py addgroupnamealias MyGroup TestGroupAlias

``addstreamalias``
==================

Allows you to create secondary name(s) for internal streams. Once an alias is
created the localstreamname cannot be used to request playback of that stream.
Once an alias is used (requested by a client) the alias is removed. Aliases
are designed to be used to protect/hide your source streams.

Arguments:

* ``localStreamName`` The original stream name.

* ``aliasName`` The alias alternative to the ``localStreamName``.

Example:
::

    ./manage.py addstreamalias bunny video1 --expire-period=-300

``createingestpoint``
=====================

Creates an RTMP ingest point.

Arguments:

* ``privateStreamName`` The name that RTMP Target Stream Names must match.

* ``publicStreamName`` The name that is used to access the stream pushed to the
  ``privateStreamName``. The ``publicStreamName`` becomes the streams
  ``localStreamName``.

Example:
::

    ./manage.py createingestpoint theIngestPoint useMeToViewStream

``flushgroupnamealiases``
=========================

Invalidates all group name aliases.

Example:
::

    ./manage.py flushgroupnamealiases

``flushstreamaliases``
======================

Invalidates all streams aliases.

Example:
::

    ./manage.py flushstreamaliases

``getconfiginfo``
=================

Returns the information of the stream by the configId.

Arguments:

* ``configId`` The ``configId`` of the configuration to get some information.

Example
::

    ./manage.py getconfiginfo 1

``getgroupnamebyalias``
=======================

Returns the group name given the alias name.

Arguments:

* ``aliasName`` The group alias name.

Example
::

    ./manage.py getgroupnamebyalias TestGroupAlias

``getstreaminfo``
=================

Returns a detailed set of information about a stream.

Arguments:

* ``idOrLocalStreamName`` The uniqueId of the stream or the name of the stream.

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

``listgroupnamealiases``
========================

Returns a complete list of group name aliases.

Example
::

    ./manage.py listgroupnamealiases

``listhttpstreamingsessions``
=============================

Lists all currently active HTTP streaming sessions.

Example
::

    ./manage.py listhttpstreamingsessions

``listingestpoints``
====================

Lists the currently available Ingest Points.

Example
::

    ./manage.py listingestpoints

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

``pullstream``
==============

Pull in a stream from an external source.

Arguments:

* ``uri`` The URI of the external stream. Can be RTMP, RTSP or unicast/multicast (d) mpegts

Parameters:

* ``--keep-alive`` If keepAlive is set to 1, the server will attempt to reestablish
  connection with a stream source after a connection has been lost. The reconnect
  will be attempted once every second.

* ``--local-stream-name`` Name of the stream. Otherwise, a fallback techniques used
  to determine the stream name (based on the URI).

* ``--force-tcp`` If 1 and if the stream is RTSP, a TCP connection will be forced.
  Otherwise the transport mechanism will be negotiated (UDP or TCP).

* ``--tc-url`` TC URL to use in the initial RTMP connect invoke.

* ``--page-url`` Originating web page address to use in the initial RTMP connect invoke.

* ``--swf-url`` Originating swf URL to use in the initial RTMP connect invoke.

* ``--range-start`` A value from which the playback should start expressed in seconds
  (RTSP and RTMP connections only).

* ``--range-end`` The length in seconds for the playback (RTSP and RTMP connections only).

* ``--ttl`` Sets the IP_TTL (time to live) option on the socket.

* ``--tos`` Sets the IP_TOS (Type of Service) option on the socket.

* ``--rtcp-detection-interval`` How much time (in seconds) should the server wait for RTCP
  packets before declaring the RTSP stream as a RTCP-less stream.

* ``--emulate-user-agent`` User agent string (only for RTMP).

* ``--is-audio`` If 1 and if the stream is RTP, it indicates that the currently pulled
  stream is an audio source. Otherwise the pulled source is assumed as a video source.

* ``--audio-codec-bytes`` The audio codec setup of RTP stream if it is audio. Represented
  as hex format without "0x" or "h".

* ``--sps-bytes`` The video SPS bytes of RTP stream if it is video. It should be base 64 encoded.

* ``--pps-bytes`` The video PPS bytes of RTP stream if it is video. It should be base 64 encoded.

* ``--ssm-ip`` The source IP from source-specific-multicast (only UDP based pull).

* ``--http-proxy`` IP:Port - specifies an RTSP HTTP Proxy from which the RTSP stream should be
  pulled; "self" - pulling RTSP over HTTP.

Example
::

    ./manage.py pullstream "rtmp://s2pchzxmtymn2k.cloudfront.net/cfx/st/mp4:sintel.mp4" --local-stream-name=testpullstream

``removeconfig``
================

Stop the stream and remove the corresponding configuration entry.

Arguments:

* ``idOrGroupName`` The ``configId`` of the configuration that needs to be removed
  or the name of the group that needs to be removed.

Example
::

    ./manage.py removeconfig 555

``removegroupnamealias``
========================

Removes an alias of a group.

Arguments:

* ``aliasName`` The alias alternative to be removed from the group name.

Example
::

    ./manage.py removegroupnamealias TestGroupAlias

``removeingestpoint``
=====================

Removes an RTMP ingest point.

Arguments:

* ``privateStreamName`` The Ingest Point is identified by the ``privateStreamName``,
  so only that is required to delete it.

Example
::

    ./manage.py removeingestpoint theIngestPoint

``removestreamalias``
=====================

Removes an alias of a stream.

Arguments:

* ``aliasName`` The alias to delete.

Example
::

    ./manage.py removestreamalias video1

``shutdownstream``
==================

Terminates a specific stream. When ``permanently=1`` is used, this command is analogous to ``removeConfig``.

Arguments:

* ``idOrLocalStreamName`` The uniqueId of the stream or the name of the inbound
  stream that needs to be terminated.

Example
::

    ./manage.py shutdownstream 55
