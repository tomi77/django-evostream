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

``pushstream``
==============

Try to push a local stream to an external destination. The pushed stream
can only use the RTMP, RTSP or MPEG-TS unicast/multicast protocol.

Arguments:

* ``uri`` The URI of the external stream. Can be RTMP, RTSP or unicast/multicast (d) mpegts.

Parameters:

* ``--keep-alive`` If keepAlive is set to 1, the server will attempt to reestablish
  connection with a stream source after a connection has been lost. The reconnect
  will be attempted once every second.

* ``--local-stream-name`` Name of the stream. Otherwise, a fallback techniques used
  to determine the stream name (based on the URI).

* ``--ratget-stream-name`` It can be one of following: **live**, **record**, **append**.
  It is meaningful only for RTMP.

* ``--tc-url`` TC URL to use in the initial RTMP connect invoke.

* ``--page-url`` Originating web page address to use in the initial RTMP connect invoke.

* ``--swf-url`` Originating swf URL to use in the initial RTMP connect invoke.

* ``--ttl`` Sets the IP_TTL (time to live) option on the socket.

* ``--tos`` Sets the IP_TOS (Type of Service) option on the socket.

* ``--emulate-user-agent`` User agent string (only for RTMP).

* ``--rtmp-absolute-timestamps`` Forces the timestamps to be absolute when using RTMP.

* ``--send-chunk-size-request`` Sets whether the RTMP stream will or will not send a
    “Set Chunk Length” message. This is significant when pushing to Akamai’s new RTMP HD
    ingest point where this parameter should be set to 0 so that Akamai will not drop the
    connection.

* ``--use-source-pts`` When value is true, timestamps on source inbound RTMP stream are
    passed directly to the outbound (pushed) RTMP streams. This affects only pushed
    Outbound Net RTMP with net RTMP source. This parameter overrides the value of the
    ``config.lua`` option of the same name.

Example
::

    ./manage.py pushstream "rtmp://DestinationAddress/live" --local-stream-name=testpullstream --target-stream-name=testpushStream

``createhlsstream``
===================

Create an HTTP Live Stream (HLS) out of an existing H.264/AAC stream.

Arguments:

* ``localStreamNames`` The stream(s) that will be used as the input. This is a comma-delimited
    list of active stream names (local stream names).

* ``targetFolder`` The folder where all the .ts/.m3u8 files will be stored. This folder must
    be accessible by the HLS clients. It is usually in the web-root of the server.

Optional:

* ``--keep-alive`` If true, the EMS will attempt to reconnect to the stream source if the
    connection is severed.

* ``--overwrite-destination`` If true, it will force overwrite of destination files.

* ``--stale-retention-count`` The number of old files kept besides the ones listed in the
    current version of the playlist (only rolling playlist).

* ``--create-master-playlist`` If true, a master playlist will be created.

* ``--cleanup-destination`` If true, all \*.ts and \*.m3u8 files in the target folder will
    be removed before HLS creation is started.

* ``--bandwidths`` The corresponding bandwidths for each stream listed in localStreamNames.
    Again, this can be a comma-delimited list.

* ``--groupName`` The name assigned to the HLS stream or group.

* ``--playlist-type``

* ``--playlist-length`` The length (number of elements) of the playlist (only rolling playlist).

* ``--playlist-name`` The file name of the playlist (\*.m3u8).

* ``--chunk-length`` The length (in seconds) of each playlist element (\*.ts file). Minimum
    value is 1 (second).

* ``--max-chunk-length`` Maximum length (in seconds) the EMS will allow any single chunk to be.

* ``--chunk-base-name`` The base name used to generate the \*.ts chunks.

* ``--chunk-on-idr`` If true, chunking is performed ONLY on IDR. Otherwise, chunking is
    performed whenever chunk length is achieved.

* ``--drm-type`` Type of DRM encryption to use.

* ``--aes-key-count`` Number of keys that will be automatically generated and rotated over
    while encrypting this HLS stream.

* ``--audio-only`` If true, stream will be audio only.

* ``--hls-resume`` If true, HLS will resume in appending segments to previously created child
    playlist even in cases of EMS shutdown or cut off stream source.

* ``--cleanup-on-close`` If true, corresponding hls files to a stream will be deleted if the
    said stream is removed or shut down or disconnected.

* ``--use-byte-range`` If true, will use the EXT-X-BYTERANGE feature of HLS (version 4 and up).

* ``--file-length`` When using useByteRange=1, this parameter needs to be set too. This
    will be the size of file before chunking it to another file, this replace the chunkLength
    in case of EXT-X-BYTERANGE, since chunkLength will be the byte range chunk.

* ``--use-system-time`` If true, uses UTC in playlist time stamp otherwise will use the local
    server time.

* ``--offset-time`` A parameter valid only for HLS v.6 onwards. This will indicate the start
    offset time (in seconds) for the playback of the playlist.

Example
::

 ./manage.py createhlsstream hlstest /MyWebRoot/ --bandwidths=128 --group-name=hls --playlist-type=rolling --playlist-length=10 --chunk-length=5

``create_hds_stream``
=====================

Create an HDS (HTTP Dynamic Streaming) stream out of an existing H.264/AAC stream.

Arguments:

* ``localStreamNames`` The stream(s) that will be used as the input.
  This is a comma-delimited list of active stream names (local stream
  names).

* ``targetFolder`` The folder where all the manifest (*.f4m) and
  fragment (f4v*) files will be stored. This folder must be accessible
  by the HDS clients. It is usually in the web-root of the server.

Optional:

* ``--bandwidths`` The corresponding bandwidths for each stream listed in
  ``localStreamNames``. Again, this can be a comma-delimited list.

* ``--chunk-base-name`` The base name used to generate the fragments.

* ``--chunk-length`` The length (in seconds) of fragments to be made.
  Minimum value is 1 (second).

* ``--chunk-on-idr`` If true, chunking is performed ONLY on IDR. Otherwise,
  chunking is performed whenever chunk length is achieved.

* ``--group-name`` The name assigned to the HDS stream or group.

* ``--keep-alive`` If true, the EMS will attempt to reconnect to the
  stream source if the connection is severed.

* ``--manifest-name`` The manifest file name.

* ``--overwrite-destination`` If true, it will allow overwrite of
  destination files.

* ``--playlist-type`` Either `appending` or `rolling`.

* ``--playlist-length`` The number of fragments before the server starts to
  overwrite the older fragments. Used only when ``--playlist-type`` is
  `rolling`. Ignored otherwise.

* ``--stale-retention-count`` The number of old files kept besides the ones
  listed in the current version of the playlist. Only applicable for
  rolling playlists.

* ``--create-master-playlist`` If true, a master playlist will be created.

* ``--cleanup-destination`` If true, all manifest and fragment files in the
  target folder will be removed before HDS creation is started.

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
