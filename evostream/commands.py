from functools import wraps
import logging

from .default import protocol

__all__ = ['pull_stream', 'list_streams_ids', 'get_stream_info',
           'list_streams', 'get_streams_count', 'shutdown_stream',
           'list_config', 'remove_config', 'get_config_info',
           'add_stream_alias', 'list_stream_aliases', 'remove_stream_alias',
           'flush_stream_aliases', 'add_group_name_alias',
           'flush_group_name_aliases', 'get_group_name_by_alias',
           'list_group_name_aliases', 'remove_group_name_alias']
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


@expected('uri', 'keepAlive', 'localStreamName', 'forceTcp', 'tcUrl', 'pageUrl',
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
    return protocol.protocol.execute('pullStream', uri=uri, **kwargs)


def list_streams_ids():
    """
    Get a list of IDs for every active stream.

    :link: http://docs.evostream.com/ems_api_definition/liststreamsids
    """
    return protocol.execute('listStreamsIds')


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
    return protocol.execute('getStreamInfo', **kwargs)


@expected('disableInternalStreams')
def list_streams(**kwargs):
    """
    Provides a detailed description of all active streams.

    :param disableInternalStreams: If this is 1 (true), internal streams
        (origin-edge related) are filtered out from the list
    :type disableInternalStreams: int

    :link: http://docs.evostream.com/ems_api_definition/liststreams
    """
    return protocol.execute('listStreams', **kwargs)


def get_streams_count():
    """
    Returns the number of active streams.

    :link: http://docs.evostream.com/ems_api_definition/getstreamscount
    """
    return protocol.execute('getStreamsCount')


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
    return protocol.execute('shutdownStream', **kwargs)


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
    return protocol.execute('listConfig')


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
    return protocol.execute('removeConfig', **kwargs)


@expected('id',)
def get_config_info(id):
    """
    Returns the information of the stream by the configId.

    :param id: The configId of the configuration to get some information
    :type id: int

    :link: http://docs.evostream.com/ems_api_definition/getconfiginfo
    """
    return protocol.execute('getConfigInfo', id=id)


@expected('localStreamName', 'aliasName', 'expirePeriod')
def add_stream_alias(localStreamName, aliasName, **kwargs):
    """
    Allows you to create secondary name(s) for internal streams. Once an alias
    is created the localstreamname cannot be used to request playback of that
    stream. Once an alias is used (requested by a client) the alias is removed.
    Aliases are designed to be used to protect/hide your source streams.

    :param localStreamName: The original stream name
    :type localStreamName: str

    :param aliasName: The alias alternative to the localStreamName
    :type aliasName: str

    :param expirePeriod: The expiration period for this alias. Negative values
        will be treated as one-shot but no longer than the absolute positive
        value in seconds, 0 means it will not expire, positive values mean the
        alias can be used multiple times but expires after this many seconds.
        The default is -600 (one-shot, 10 mins)
    :type expirePeriod: int

    :link: http://docs.evostream.com/ems_api_definition/addstreamalias
    """
    return protocol.execute('addStreamAlias', localStreamName=localStreamName, aliasName=aliasName, **kwargs)


def list_stream_aliases():
    """
    Returns a complete list of aliases.

    :link: http://docs.evostream.com/ems_api_definition/liststreamaliases
    """
    return protocol.execute('listStreamAliases')


@expected('aliasName',)
def remove_stream_alias(aliasName):
    """
    Removes an alias of a stream.

    :param aliasName: The alias to delete
    :type aliasName: str

    :link: http://docs.evostream.com/ems_api_definition/removestreamalias
    """
    return protocol.execute('removeStreamAlias', aliasName=aliasName)


def flush_stream_aliases():
    """
    Invalidates all streams aliases.

    :link: http://docs.evostream.com/ems_api_definition/flushstreamaliases
    """
    return protocol.execute('flushStreamAliases')


@expected('groupName', 'aliasName')
def add_group_name_alias(groupName, aliasName):
    """
    Creates secondary name(s) for group names. Once an alias is created the
    group name cannot be used to request HTTP playback of that stream. Once
    an alias is used (requested by a client) the alias is removed. Aliases are
    designed to be used to protect/hide your source streams.

    :param groupName: The original group name
    :type groupName: str

    :param aliasName: The alias alternative to the group name
    :type aliasName: str

    :link: http://docs.evostream.com/ems_api_definition/addgroupnamealias
    """
    return protocol.execute('addGroupNameAlias', groupName=groupName,
                            aliasName=aliasName)


def flush_group_name_aliases():
    """
    Invalidates all group name aliases.

    :link: http://docs.evostream.com/ems_api_definition/flushgroupnamealiases
    """
    return protocol.execute('flushGroupNameAliases')


@expected('aliasName')
def get_group_name_by_alias(aliasName):
    """
    Returns the group name given the alias name.

    :param aliasName: The original group name
    :type aliasName: str

    :link: http://docs.evostream.com/ems_api_definition/getgroupnamebyalias
    """
    return protocol.execute('getGroupNameByAlias', aliasName=aliasName)


def list_group_name_aliases():
    """
    Returns a complete list of group name aliases.

    :link: http://docs.evostream.com/ems_api_definition/listgroupnamealiases
    """
    return protocol.execute('listGroupNameAliases')


@expected('aliasName')
def remove_group_name_alias(aliasName):
    """
    Removes an alias of a group.

    :param aliasName: The alias alternative to be removed from the group name.
    :type aliasName: str

    :return: http://docs.evostream.com/ems_api_definition/removegroupnamealiases
    """
    return protocol.execute('removeGroupNameAlias', aliasName=aliasName)
