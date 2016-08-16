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

``push_stream``
===============

Try to push a local stream to an external destination. The pushed stream
can only use the RTMP, RTSP or MPEG-TS unicast/multicast protocol.

Required

:``uri`` `(str)`:
    The URI of the external stream. Can be RTMP, RTSP or unicast/multicast
    (d) mpegts.

Optional

:``keepAlive`` `(int)`:
    If ``keepAlive`` is set to 1, the server will attempt to reestablish
    connection with a stream source after a connection has been lost. The
    reconnect will be attempted once every second.

:``localStreamName`` `(str)`:
    If provided, the stream will be given this name. Otherwise, a fallback
    techniques used to determine the stream name (based on the URI).

:``targetStreamName`` `(str)`:
    The name of the stream at destination. If not provided, the target
    stream name will be the same as the local stream name.

:``targetStreamType`` `(str)`:
    It can be one of following: **live**, **record**, **append**. It is
    meaningful only for RTMP.

:``tcUrl`` `(str)`:
    When specified, this value will be used to set the TC URL in the initial
    RTMP connect invoke.

:``pageUrl`` `(str)`:
    When specified, this value will be used to set the originating web page
    address in the initial RTMP connect invoke.

:``swfUrl`` `(str)`:
    When specified, this value will be used to set the originating swf URL
    in the initial RTMP connect invoke.

:``ttl`` `(int)`:
    Sets the IP_TTL (time to live) option on the socket.

:``tos`` `(int)`:
    Sets the IP_TOS (Type of Service) option on the socket.

:``emulateUserAgent`` `(str)`:
    When specified, this value will be used as the user agent string.
    It is meaningful only for RTMP.

:``rtmpAbsoluteTimestamps`` `(int)`:
    Forces the timestamps to be absolute when using RTMP.

:``sendChunkSizeRequest`` `(int)`:
    Sets whether the RTMP stream will or will not send a "Set Chunk Length"
    message. This is significant when pushing to Akamai’s new RTMP HD
    ingest point where this parameter should be set to 0 so that Akamai will
    not drop the connection.

:``useSourcePts`` `(int)`:
    When value is true, timestamps on source inbound RTMP stream are passed
    directly to the outbound (pushed) RTMP streams. This affects only pushed
    Outbound Net RTMP with net RTMP source. This parameter overrides the
    value of the config.lua option of the same name.

Example
::

 push_stream('rtmp://DestinationAddress/live' localStreamName='testpullstream' targetStreamName='testpushStream')

http://docs.evostream.com/ems_api_definition/pushstream

``create_hls_stream``
=====================

Create an HTTP Live Stream (HLS) out of an existing H.264/AAC stream. HLS
is used to stream live feeds to iOS devices such as iPhones and iPads.

Required:

:``localStreamNames`` `(str)`: The stream(s) that will be used as the input.
    This is a comma-delimited list of active stream names (local stream names).

:``targetFolder`` `(str)`: The folder where all the .ts/.m3u8 files will be
    stored. This folder must be accessible by the HLS clients. It is
    usually in the web-root of the server.

Optional:

:``keepAlive`` `(int)`: If true, the EMS will attempt to reconnect to the
    stream source if the connection is severed.

:``overwriteDestination`` `(int)`: If true, it will force overwrite of
    destination files.

:``staleRetentionCount`` `(int)`: The number of old files kept besides the ones
    listed in the current version of the playlist. Only applicable for
    rolling playlists.

:``createMasterPlaylist`` `(int)`: If true, a master playlist will be created.

:``cleanupDestination`` `(int)`: If true, all \*.ts and \*.m3u8 files in the
    target folder will be removed before HLS creation is started.

:``bandwidths`` `(int)`: The corresponding bandwidths for each stream listed in
    localStreamNames. Again, this can be a comma-delimited list.

:``groupName`` `(str)`: The name assigned to the HLS stream or group. If the
    localStreamNames parameter contains only one entry and groupName is
    not specified, groupName will have the value of the input stream name.

:``playlistType`` `(str)`: Either appending or rolling.

:``playlistLength`` `(int)`: The length (number of elements) of the playlist.
    Used only when playlistType is rolling. Ignored otherwise.

:``playlistName`` `(str)`: The file name of the playlist (\*.m3u8).

:``chunkLength`` `(int)`: The length (in seconds) of each playlist element (\*.ts
    file). Minimum value is 1 (second).

:``maxChunkLength`` `(int)`: Maximum length (in seconds) the EMS will allow any
    single chunk to be. This is primarily in the case of chunkOnIDR=true where
    the EMS will wait for the next key-frame. If the maxChunkLength is less than
    chunkLength, the parameter shall be ignored.

:``chunkBaseName`` `(str)`: The base name used to generate the \*.ts chunks.

:``chunkOnIDR`` `(int)`: If true, chunking is performed ONLY on IDR. Otherwise,
    chunking is performed whenever chunk length is achieved.

:``drmType`` `(str)`: Type of DRM encryption to use. Options are: none
    (no encryption), evo (AES Encryption), SAMPLE-AES (Sample-AES),
    verimatrix (Verimatrix DRM). For Verimatrix DRM, the "drm" section of
    the config.lua file must be active and properly configured.

:``AESKeyCount`` `(int)`: Number of keys that will be automatically generated
    and rotated over while encrypting this HLS stream.

:``audioOnly`` `(int)`: If true, stream will be audio only.

:``hlsResume`` `(int)`: If true, HLS will resume in appending segments to
    previously created child playlist even in cases of EMS shutdown or cut
    off stream source.

:``cleanupOnClose`` `(int)`: If true, corresponding hls files to a stream will
    be deleted if the said stream is removed or shut down or disconnected.

:``useByteRange`` `(int)`: If true, will use the EXT-X-BYTERANGE feature of HLS
    (version 4 and up).

:``fileLength`` `(int)`: When using useByteRange=1, this parameter needs to be
    set too. This will be the size of file before chunking it to another
    file, this replace the chunkLength in case of EXT-X-BYTERANGE, since
    chunkLength will be the byte range chunk.

:``useSystemTime`` `(int)`: If true, uses UTC in playlist time stamp otherwise
    will use the local server time.

:``offsetTime`` `(int)`:

:``startOffset`` `(int)`: A parameter valid only for HLS v.6 onwards. This will
    indicate the start offset time (in seconds) for the playback of the
    playlist.

Example
::

 create_hls_stream('hlstest', '/MyWebRoot/', bandwidths=128, groupName='hls', playlistType='rolling', playlistLength=10, chunkLength=5)

http://docs.evostream.com/ems_api_definition/createhlsstream

``create_hds_stream``
=====================

Create an HDS (HTTP Dynamic Streaming) stream out of an existing H.264/AAC
stream. HDS is used to stream standard MP4 media over regular HTTP
connections.

Required:

:``localStreamNames`` `(str)`: The stream(s) that will be used as the input.
    This is a comma-delimited list of active stream names (local stream
    names).

:``targetFolder`` `(str)`: The folder where all the manifest (*.f4m) and
    fragment (f4v*) files will be stored. This folder must be accessible by
    the HDS clients. It is usually in the web-root of the server.

Optional:

:``bandwidths`` `(int)`: The corresponding bandwidths for each stream listed in
    localStreamNames. Again, this can be a comma-delimited list.

:``chunkBaseName`` `(str)`: The base name used to generate the fragments.

:``chunkLength`` `(int)`: The length (in seconds) of fragments to be made.
    Minimum value is 1 (second)

:``chunkOnIDR`` `(int)`: If true, chunking is performed ONLY on IDR. Otherwise,
    chunking is performed whenever chunk length is achieved.

:``groupName`` `(str)`: The name assigned to the HDS stream or group. If the
    ``localStreamNames`` parameter contains only one entry and ``groupName`` is
    not specified, ``groupName`` will have the value of the input stream name.

:``keepAlive`` `(int)`: If true, the EMS will attempt to reconnect to the
    stream source if the connection is severed.

:``manifestName`` `(str)`: The manifest file name.

:``overwriteDestination`` `(int)`: If true, it will allow overwrite of
    destination files.

:``playlistType`` `(str)`: Either `appending` or `rolling`.

:``playlistLength`` `(int)`: The number of fragments before the server starts to
    overwrite the older fragments. Used only when ``playlistType`` is
    `rolling`. Ignored otherwise.
:type playlistLength: int

:``staleRetentionCount`` `(int)`: The number of old files kept besides the ones
    listed in the current version of the playlist. Only applicable for
    `rolling` playlists.

:``createMasterPlaylist`` `(int)`: If true, a master playlist will be created.

:``cleanupDestination`` `(int)`: If true, all manifest and fragment files in the
    target folder will be removed before HDS creation is started.

Example
::

 create_hds_stream('testpullStream', '../evo-webroot', groupName='hds', playlistType='rolling')

http://docs.evostream.com/ems_api_definition/createhdsstream

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
