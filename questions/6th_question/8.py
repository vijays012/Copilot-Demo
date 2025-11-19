#Prompt given to copilot-
# create a memoization decorator
def memoize(func):
    cache = {}     
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return memoized_func

# Identified bug in the above code:
# Bug: cache={} is a mutable default value → causes functions to share the same cache.


# Fixed code : 
from functools import wraps

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper