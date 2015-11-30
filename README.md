# easy-memcache

A flask style memcached high-level interfac for python.It's easy to manage your memcached keys,when you use this package.

##usage


```python
import memcache
from easy_memcache import CacheManager
mc = memcache.Client()
mc_manager = CacheManager(mc)

@mc_manager.register("/some-value", 60)
def get_some_value():
    return "some value"    
    
@mc_manager.register("/some-value/<some_condition>", 60)
def get_some_value_with_condition(some_condition):
    return "some value with condition {}".format(some_condition)
```
