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

 push_stream('rtmp://192.168.1.2', localStreamName='testpullStream',
             targetStreamName='testpushStream')

http://docs.evostream.com/ems_api_definition/pullstream
