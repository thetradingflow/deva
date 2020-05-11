#!/usr/bin/env python
"""公共总线流.

Exsample::

    f = range+sum
    ff = f^debug
    '123'>>ff
    #函数异常将被发到debug，并且push到钉钉
"""
import logging
from .namespace import NS, NT
import datetime
# from .endpoints import Dtalk

__all__ = [
    'log', 'warn', 'debug', 'bus'
]

warn = NS('warn')
warn.sink(logging.warning)


def log_print(x):
    print(datetime.datetime.now(), ':', x)


log = NS('log', cache_max_len=10, cache_max_age_seconds=60 * 60 * 24)
log.sink(log_print)


bus = NT('bus')

debug = NS('debug')
# debug.map(str).unique() >> Dtalk()
