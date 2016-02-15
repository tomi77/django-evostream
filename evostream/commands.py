from .default import protocol
from .utils import check_params


execute = protocol.execute


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


def shutdown_stream(**kwargs):
    """
    Delete stream.
    """
    expected = ['id', 'name', 'permanently']
    check_params(expected, kwargs.keys())
    return execute('shutdownstream', **kwargs)


def list_config():
    """
    Returns a list with all push/pull configurations.
    """
    return execute('listconfig')


def remove_config(**kwargs):
    """
    This command will both stop the stream and remove the corresponding
    configuration entry. This command is the same as performing:
    <code>
    shutdownStream permanently=1
    </code>
    """
    expected = ['id', 'HlsHdsGroup', 'removeHlsHdsFiles']
    check_params(expected, kwargs.keys())
    return execute('removeconfig', **kwargs)
