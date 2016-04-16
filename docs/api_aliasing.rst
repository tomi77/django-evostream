.. _ref-api_aliasing:

========
Aliasing
========

``add_stream_alias``
====================

Allows you to create secondary name(s) for internal streams. Once an alias is
created the localstreamname cannot be used to request playback of that stream.
Once an alias is used (requested by a client) the alias is removed. Aliases
are designed to be used to protect/hide your source streams.

Required:

:``localStreamName`` `(str)`:
    The original stream name.

:``aliasName`` `(str)`:
    The alias alternative to the `localStreamName`.

Optional:

:``expirePeriod`` `(int)`:
    The expiration period for this alias. Negative values will be treated as
    one-shot but no longer than the absolute positive value in seconds,
    0 means it will not expire, positive values mean the alias can be used
    multiple times but expires after this many seconds.
    The default is -600 (one-shot, 10 mins).

Example:
::

 add_stream_alias('bunny', 'video1', expirePeriod=-300)

http://docs.evostream.com/ems_api_definition/addstreamalias

``list_stream_aliases``
=======================

Returns a complete list of aliases.

Example:
::

 list_stream_aliases()

http://docs.evostream.com/ems_api_definition/liststreamaliases

``remove_stream_alias``
=======================

Removes an alias of a stream.

Required:

:``aliasName`` `(str)`:
    The alias to delete

Example:
::

 remove_stream_alias('video1')

http://docs.evostream.com/ems_api_definition/removestreamalias

``flush_stream_aliases``
========================

Invalidates all streams aliases.

Example:
::

 flush_stream_aliases()

http://docs.evostream.com/ems_api_definition/flushstreamaliases

``add_group_name_alias``
========================

Create secondary name for group name.

Example:
::

 add_group_name_alias(groupName='MyGroup', aliasName='TestGroupAlias')

http://docs.evostream.com/ems_api_definition/addgroupnamealias

``flush_group_name_aliases``
============================

Invalidates all group name aliases.

Example:
::

 flush_group_name_aliases()

http://docs.evostream.com/ems_api_definition/flushgroupnamealiases

``get_group_name_by_alias``
===========================

Returns the group name given the alias name.

Example:
::

 get_group_name_by_alias(aliasName='TestGroupAlias')

http://docs.evostream.com/ems_api_definition/getgroupnamebyalias

``list_group_name_aliases``
===========================

Returns a complete list of group name aliases.

Example:
::

 list_group_name_aliases()

http://docs.evostream.com/ems_api_definition/listgroupnamealiases

``remove_group_name_alias``
===========================

Removes an alias of a group.

Example:
::

 remove_group_name_alias()

http://docs.evostream.com/ems_api_definition/removegroupnamealiases
