# -*- coding: utf-8 -*-
# https://github.com/suqin/easy-memcache
__author__ = 'qjphh003@163.com'

import re

class CacheManager():
    def __init__(self, mc):
        self.mc = mc
        self.routes = []

    def set(self, key, value, timeout=30):
        if value == None:
            raise ValueError("the value of key: '%s' should not be None" % key)
        self.mc.set(key, value, timeout)

    def get(self, key):
        value = self.mc.get(key)
        if not value:
            route_match = self.get_route_match(key)
            if route_match:
                kwargs, view_function, timeout = route_match
                value = view_function(**kwargs)
                self.set(key, value, timeout)
            else:
                raise ValueError('Route "{}"" has not been registered'.format(key))
        return value

    def remove(self, key):
        return self.mc.delete(key)

    @staticmethod
    def build_route_pattern(route):
        route_regex = re.sub(r'(<\w+>)', r'(?P\1.+)', route)
        return re.compile("^{}$".format(route_regex))

    def register(self, route_str, timeout):
        def decorator(f):
            route_pattern = self.build_route_pattern(route_str)
            self.routes.append((route_pattern, f, timeout))
            return f
        return decorator


    def get_route_match(self, path):
        for route_pattern, view_function, timeout in self.routes:
            m = route_pattern.match(path)
            if m:
               return m.groupdict(), view_function, timeout
        return None