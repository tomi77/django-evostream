.. _ref-api_streams:

=======
Streams
=======

``pull_stream``
===============

This will try to pull in a stream from an external source. Once a stream
has been successfully pulled it is assigned a 'local stream name' which can
be used to access the stream from the EMS.

Required:

:``uri`` `(str)`:
    The URI of the external stream. Can be RTMP, RTSP or
    unicast/multicast (d) mpegts

Optional:

:``keepAlive`` `(int)`:
    If keepAlive is set to 1, the server will attempt to
    reestablish connection with astream source after a connection has been
    lost. The reconnect will be attempted once every second
    (default: 1 true)

:``localStreamName`` `(str)`:
    If provided, the stream will be given this
    name. Otherwise, a fallback techniqueis used to determine the stream
    name (based on the URI)

:``forceTcp`` `(int)`:
    If 1 and if the stream is RTSP, a TCP connection will
    be forced. Otherwise the transport mechanism will be negotiated (UDP
    or TCP) (default: 1 true)

:``tcUrl`` `(str)`:
    When specified, this value will be used to set the TC URL in
    the initial RTMPconnect invoke

:``pageUrl`` `(str)`:
    When specified, this value will be used to set the
    originating web page address inthe initial RTMP connect invoke

:``swfUrl`` `(str)`:
    When specified, this value will be used to set the
    originating swf URL in theinitial RTMP connect invoke

:``rangeStart`` `(int)`:
    For RTSP and RTMP connections.  A value fromwhich the
    playback should start expressed in seconds. There are 2 specialvalues:
    -2 and -1. For more information, please read about start/len
    parameters here: http://livedocs.adobe.com/flashmediaserver/3.0/hpdocs/help.html?content=00000185.html

:``rangeEnd`` `(int)`:
    The length in seconds for the playback. -1 is a special
    value. For more information, please read about start/len parameters
    here: http://livedocs.adobe.com/flashmediaserver/3.0/hpdocs/help.html?content=00000185.html

:``ttl`` `(int)`:
    Sets the IP_TTL (time to live) option on the socket

:``tos`` `(int)`:
    Sets the IP_TOS (Type of Service) option on the socket

:``rtcpDetectionInterval`` `(int)`:
    How much time (in seconds) should the server
    wait for RTCP packets before declaring the RTSP stream as a RTCP-less
    stream

:``emulateUserAgent`` `(str)`:
    When specified, this value will be used as the
    user agent string. It is meaningful only for RTMP

:``isAudio`` `(int)`:
    If 1 and if the stream is RTP, it indicates that the
    currently pulled stream is an audio source. Otherwise the pulled
    source is assumed as a video source

:``audioCodecBytes`` `(str)`:
    The audio codec setup of this RTP stream if it is
    audio. Represented as hex format without ‘0x’ or ‘h’. For example:
    audioCodecBytes=1190

:``spsBytes`` `(str)`:
    The video SPS bytes of this RTP stream if it is video. It
    should be base 64 encoded.

:``ppsBytes`` `(str)`:
    The video PPS bytes of this RTP stream if it is video. It
    should be base 64 encoded

:``ssmIp`` `(str)`:
    The source IP from source-specific-multicast. Only usable
    when doing UDP based pull

:``httpProxy`` `(str)`:
    This parameter has two valid values: IP:Port – This
    value combination specifies an RTSP HTTP Proxy from which the RTSP
    stream should be pulled from Self - Specifying “self” as the value
    implies pulling RTSP over HTTP

Example::

 pull_stream('rtmp://s2pchzxmtymn2k.cloudfront.net/cfx/st/mp4:sintel.mp4', localStreamName='testpullStream')

http://docs.evostream.com/ems_api_definition/pullstream

``list_streams_ids``
====================

Get a list of IDs for every active stream.

Example
::

    list_streams_ids()

http://docs.evostream.com/ems_api_definition/liststreamsids

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

``get_streams_count``
=====================

Returns the number of active streams.

Example
::

    get_streams_count()

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

``get_config_info``
===================

Returns the information of the stream by the `configId`.

Required:

:``id`` `(int)`:
    The `configId` of the configuration to get some information.

Example:
::

 get_config_info(id=1)

http://docs.evostream.com/ems_api_definition/getconfiginfo
