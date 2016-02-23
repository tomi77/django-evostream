================
django-evostream
================

.. image:: https://codeclimate.com/github/tomi77/django-evostream/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/django-evostream
   :alt: Code Climate

Installation
============

Install package via ``pip``
::

    pip install django-evostream

Setup ``EvoStream Media Server`` HTTP API address
::

    EVOSTREAM_URL = '127.0.0.1:7777'

API Usage
=========

::

    from evostream.commands import list_streams

    print list_streams()

CLI Usage
=========

``django-evostream`` provide ``Django`` commands to manage ``EvoStream Media Server``.

Example
::

    ./manage.py liststreams
