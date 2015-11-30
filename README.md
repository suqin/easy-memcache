# easy-memcache

A flask style memcached high-level interfac for python.It's easy to manage your memcached keys when you use this package.

##usage

To begin we'll declare callback function and memcached keys pattern:
```python
import memcache
from easy_memcache import CacheManager
mc = memcache.Client()
mc_manager = CacheManager(mc)

@mc_manager.register("/some-value", 60)
def get_some_value():
    return "some value"    
    
@mc_manager.register("/another-value/<some_condition>", 60)
def get_another_value_with_condition(some_condition):
    return "another value with condition {}".format(some_condition)
```

then we can get values from memcached like this:
```python
some_value = mc_manager.get("/some-value")
another_value_with_comdition = mc_manager.get("/another-value/1")
```
First, mc_manager will check the keys pattern and get a key.Then mc_manager will check the memcached server.If mc_manager get the value of the key,return it,else, mc_manager will call the callback function to get value,then ,save the value and return it.

To update the value in memcached:
```python
mc_manager.remove('/some-value')
```

