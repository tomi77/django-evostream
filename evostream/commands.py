from functools import wraps
import logging

from .default import protocol


execute = protocol.execute
logger = logging.getLogger(__name__)


def expected(*expected_keys):
    expected_keys = set(expected_keys)

    def command_decorator(func):
        def wrapped_func(*args, **kwargs):
            unexpected = set(kwargs.keys()) - expected_keys

            if bool(unexpected):
                unexpected = ', '.join([key for key in list(unexpected)])
                logger.warning('Function %s: Unexpected argument(s): %s', func.__name__, unexpected)

            kwargs = dict((key, val) for key, val in kwargs.items()
                          if key in expected_keys)

            return func(*args, **kwargs)
        return wraps(func)(wrapped_func)
    return command_decorator


@expected('keepAlive', 'localStreamName', 'forceTcp', 'tcUrl', 'pageUrl',
          'swfUrl', 'ttl', 'tos', 'rtcpDetectionInterval', 'emulateUserAgent',
          'isAudio', 'audioCodecBytes', 'spsBytes', 'ppsBytes', 'ssmIp')
def pull_stream(uri, **kwargs):
    """
    This will try to pull in a stream from an external source. Once a stream
    has been successfully pulled it is assigned a 'local stream name' which can
    be used to access the stream from the EMS.

    :param uri: The URI of the external stream. Can be RTMP, RTSP or
        unicast/multicast (d) mpegts
    :type uri: str

    :param keepAlive: If keepAlive is set to 1, the server will attempt to
        reestablish connection with astream source after a connection has been
        lost. The reconnect will be attempted once every second
        (default: 1 true)
    :type keepAlive: int

    :param localStreamName: If provided, the stream will be given this
        name. Otherwise, a fallback techniqueis used to determine the stream
        name (based on the URI)
    :type localStreamName: str

    :param forceTcp: If 1 and if the stream is RTSP, a TCP connection will
        be forced. Otherwise the transport mechanism will be negotiated (UDP
        or TCP) (default: 1 true)
    :type forceTcp: int

    :param tcUrl: When specified, this value will be used to set the TC URL in
        the initial RTMPconnect invoke
    :type tcUrl: str

    :param pageUrl: When specified, this value will be used to set the
        originating web page address inthe initial RTMP connect invoke
    :type pageUrl: str

    :param swfUrl: When specified, this value will be used to set the
        originating swf URL in theinitial RTMP connect invoke
    :type swfUrl: str

    :param rangeStart: For RTSP and RTMP connections.  A value fromwhich the
        playback should start expressed in seconds. There are 2 specialvalues:
        -2 and -1. For more information, please read about start/len
        parameters here:
        http://livedocs.adobe.com/flashmediaserver/3.0/hpdocs/help.html?content=00000185.html
    :type rangeStart: int

    :param rangeEnd: The length in seconds for the playback. -1 is a special
        value. For more information, please read about start/len parameters
        here:
        http://livedocs.adobe.com/flashmediaserver/3.0/hpdocs/help.html?content=00000185.html
    :type rangeEnd: int

    :param ttl: Sets the IP_TTL (time to live) option on the socket
    :type ttl: int

    :param tos: Sets the IP_TOS (Type of Service) option on the socket
    :type tos: int

    :param rtcpDetectionInterval: How much time (in seconds) should the server
        wait for RTCP packets before declaring the RTSP stream as a RTCP-less
        stream
    :type rtcpDetectionInterval: int

    :param emulateUserAgent: When specified, this value will be used as the
        user agent string. It is meaningful only for RTMP
    :type emulateUserAgent: str

    :param isAudio: If 1 and if the stream is RTP, it indicates that the
        currently pulled stream is an audio source. Otherwise the pulled
        source is assumed as a video source
    :type isAudio: int

    :param audioCodecBytes: The audio codec setup of this RTP stream if it is
        audio. Represented as hex format without '0x' or 'h'. For example:
        audioCodecBytes=1190
    :type audioCodecBytes: str

    :param spsBytes: The video SPS bytes of this RTP stream if it is video. It
        should be base 64 encoded.
    :type spsBytes: str

    :param ppsBytes: The video PPS bytes of this RTP stream if it is video. It
        should be base 64 encoded
    :type ppsBytes: str

    :param ssmIp: The source IP from source-specific-multicast. Only usable
        when doing UDP based pull
    :type ssmIp: str

    :param httpProxy: This parameter has two valid values: IP:Port - This
        value combination specifies an RTSP HTTP Proxy from which the RTSP
        stream should be pulled from Self - Specifying "self" as the value
        implies pulling RTSP over HTTP
    :type httpProxy: str

    :link: http://docs.evostream.com/ems_api_definition/pullstream
    """
    return execute('pullstream', uri=uri, **kwargs)


@expected('id', 'localStreamName')
def get_stream_info(**kwargs):
    """
    Returns a detailed set of information about a stream.

    :param id: The uniqueId of the stream. Usually a value returned by
        listStreamsIDs. This parameter is not mandatory but either this or the
        localStreamName should be present to identify the particular stream
    :type id: int

    :param localStreamName: The name of the stream. This parameter is not
        mandatory but either this or the id should be present to identify the
        particular stream
    :type localStreamName: str

    :link: http://docs.evostream.com/ems_api_definition/getstreaminfo
    """
    return execute('getstreaminfo', **kwargs)


@expected('disableInternalStreams')
def list_streams(**kwargs):
    """
    Provides a detailed description of all active streams.

    :param disableInternalStreams: If this is 1 (true), internal streams
        (origin-edge related) are filtered out from the list
    :type disableInternalStreams: int

    :link: http://docs.evostream.com/ems_api_definition/liststreams
    """
    return execute('liststreams', **kwargs)


@expected('id', 'localStreamName', 'permanently')
def shutdown_stream(**kwargs):
    """
    Terminates a specific stream. When permanently=1 is used, this command is
    analogous to removeConfig.

    :param id: The uniqueId of the stream that needs to be terminated. The
        stream ID's can be obtained using the listStreams command. This
        parameter is not mandatory but either this or localStreamName should be
        present to identify the particular stream
    :type id: int

    :param localStreamName: The name of the inbound stream which you wish to
        terminate. This will also terminate any outbound streams that are
        dependent upon this input stream. This parameter is not mandatory but
        either this or the id should be present to identify the particular
        stream
    :type localStreamName: str

    :param permanently: If true, the corresponding push/pull configuration will
        also be terminated. Therefore, the stream will NOT be reconnected when
        the server restarts
    :type permanently: int

    :link: http://docs.evostream.com/ems_api_definition/shutdownstream
    """
    return execute('shutdownstream', **kwargs)


def list_config():
    """
    Returns a list with all push/pull configurations.

    Whenever the pullStream or pushStream interfaces are called, a record
    containing the details of the pull or push is created in the
    pullpushconfig.xml file. Then, the next time the EMS is started, the
    pullpushconfig.xml file is read, and the EMS attempts to reconnect all of
    the previous pulled or pushed streams.

    :link: http://docs.evostream.com/ems_api_definition/listconfig
    """
    return execute('listconfig')


@expected('id', 'groupName', 'removeHlsHdsFiles')
def remove_config(**kwargs):
    """
    This command will both stop the stream and remove the corresponding
    configuration entry. This command is the same as performing
    shutdownStream permanently=1.

    :param id: The configId of the configuration that needs to be removed.
        ConfigId's can be obtained from the listConfig interface. Removing an
        inbound stream will also automatically remove all associated outbound
        streams.
    :type id: int

    :param groupName: The name of the group that needs to be removed
        (applicable to HLS, HDS and external processes). Mandatory only if the
        id parameter is not specified.
    :type groupName: str

    :param removeHlsHdsFiles: If 1 (true) and the stream is HLS or HDS, the
        folder associated with it will be removed
    :type removeHlsHdsFiles: int

    :link: http://docs.evostream.com/ems_api_definition/removeconfig
    """
    return execute('removeconfig', **kwargs)
