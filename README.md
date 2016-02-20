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

    from evostream.commands import list_streams

    print list_streams()

## CLI Usage

`django-evostream` provide `Django` commands to manage `EvoStream`.

Example:

    ./manage.py liststreams

## Documentation

http://pythonhosted.org/django-evostream/