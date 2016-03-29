================
django-evostream
================

.. image:: https://codeclimate.com/github/tomi77/django-evostream/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/django-evostream
   :alt: Code Climate
.. image:: https://travis-ci.org/tomi77/django-evostream.svg?branch=master
   :target: https://travis-ci.org/tomi77/django-evostream
.. image:: https://coveralls.io/repos/github/tomi77/django-evostream/badge.svg?branch=master
   :target: https://coveralls.io/github/tomi77/django-evostream?branch=master

Installation
============

Install package via ``pip``
::

    pip install django-evostream

Setup ``EvoStream Media Server`` HTTP API address
::

    EVOSTREAM_URI = 'http://127.0.0.1:7777'

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
