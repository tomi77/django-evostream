from .default import protocol
from .utils import check_params


execute = protocol.execute


def pullstream(uri, **kwargs):
    """
    This will try to pull in a stream from an external source. Once a stream
    has been successfully pulled it is assigned a 'local stream name' which can
    be used to access the stream from the EMS.
    """
    kwargs['uri'] = uri
    expected = ['uri', 'keepAlive', 'localStreamName', 'forceTcp', 'tcUrl', 'pageUrl', 'swfUrl', 'ttl', 'tos',
                'rtcpDetectionInterval', 'emulateUserAgent', 'isAudio', 'audioCodecBytes', 'spsBytes', 'ppsBytes',
                'ssmIp']
    check_params(expected, kwargs.keys())
    return execute('pullstream', kwargs)


def getstreaminfo(id):
    """
    Returns a detailed set of information about a stream.
    """
    return execute('getstreaminfo', {'id': id})


def liststreams():
    """
    Provides a detailed description of all active streams.
    """
    return execute('liststreams')


def shutdownstream(**kwargs):
    """
    Delete stream.
    """
    expected = ['id', 'name', 'permanently']
    check_params(expected, kwargs.keys())
    return execute('shutdownstream', kwargs)


def listconfig():
    """
    Returns a list with all push/pull configurations.
    """
    return execute('listconfig')


def removeconfig(**kwargs):
    """
    This command will both stop the stream and remove the corresponding
    configuration entry. This command is the same as performing:
    <code>
    shutdownStream permanently=1
    </code>
    """
    expected = ['id', 'HlsHdsGroup', 'removeHlsHdsFiles']
    check_params(expected, kwargs.keys())
    return execute('removeconfig', kwargs)
