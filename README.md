# django-evostream

[![Code Climate](https://codeclimate.com/github/tomi77/django-evostream/badges/gpa.svg)](https://codeclimate.com/github/tomi77/django-evostream)

## Installation

Install package via `pip`:

    pip install django-evostream

Activate `Django` application:

    INSTALLED_APPS = (
        ...
        'evostream',
        ...
    )

Setup `EvoStream` HTTP API address:

    EVOSTREAM_URL = '127.0.0.1:7777'

## API Usage

    from evostream.commands import liststreams

    print liststreams()

### Available commands

#### pullstream(uri)

This will try to pull in a stream from an external source. Once a stream has been successfully pulled it is assigned a 'local stream name' which can be used to access the stream from the EMS.

#### getstreaminfo(id)

Returns a detailed set of information about a stream.

#### liststreams()

Provides a detailed description of all active streams.

#### shutdownstream()

Delete stream

#### listconfig()

Returns a list with all push/pull configurations.

#### removeconfig()

This command will both stop the stream and remove the corresponding configuration entry. This command is the same as performing:

    shutdownStream permanently=1

## CLI Usage

`django-evostream` provide `Django` commands to manage `EvoStream`.

### Available commands

#### List all active streams

    ./manage.py liststreams
