"""
geometrycache
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import logging
import weakref

log = logging.getLogger(__name__)

_caches = []


class GeometryCache(dict):

    def __init__(self, *a, **kwargs):
        super().__init__(*a, **kwargs)
        _caches.append(weakref.ref(self))


def cache_stats():
    lines = []
    for cache_ref in _caches:
        cache = cache_ref()
        if cache is None:
            continue

        size = sum(a.size for a in cache.values())
        lines.append(f"{size / 1024:.2f} kb")

    return "\n".join(lines)
