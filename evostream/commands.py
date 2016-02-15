from functools import wraps

from .default import protocol


execute = protocol.execute


def expected(*expected_keys):
    expected_keys = set(expected_keys)

    def command_decorator(func):
        def wrapped_view(*args, **kwargs):
            got = set(kwargs.keys())
            if bool(got - expected_keys):
                unexpected = ','.join([key for key in list(got - expected_keys)])
                raise KeyError('Unexpected argument(s): %s' % unexpected)
            return func(*args, **kwargs)
        return wraps(func)(wrapped_view)
    return command_decorator


@expected('keepAlive', 'localStreamName', 'forceTcp', 'tcUrl', 'pageUrl',
          'swfUrl', 'ttl', 'tos', 'rtcpDetectionInterval', 'emulateUserAgent',
          'isAudio', 'audioCodecBytes', 'spsBytes', 'ppsBytes', 'ssmIp')
def pull_stream(uri, **kwargs):
    """
    This will try to pull in a stream from an external source. Once a stream
    has been successfully pulled it is assigned a 'local stream name' which can
    be used to access the stream from the EMS.
    """
    return execute('pullstream', uri=uri, **kwargs)


def get_stream_info(id):
    """
    Returns a detailed set of information about a stream.
    """
    return execute('getstreaminfo', id=id)


def list_streams():
    """
    Provides a detailed description of all active streams.
    """
    return execute('liststreams')


@expected('id', 'name', 'permanently')
def shutdown_stream(**kwargs):
    """
    Delete stream.
    """
    return execute('shutdownstream', **kwargs)


def list_config():
    """
    Returns a list with all push/pull configurations.
    """
    return execute('listconfig')


@expected('id', 'HlsHdsGroup', 'removeHlsHdsFiles')
def remove_config(**kwargs):
    """
    This command will both stop the stream and remove the corresponding
    configuration entry. This command is the same as performing:
    <code>
    shutdownStream permanently=1
    </code>
    """
    return execute('removeconfig', **kwargs)
