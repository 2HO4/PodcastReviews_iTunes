# MODIFY CLASS
# ----------------------------------------------------------------------------------------------------------------


# INITIATION ------------

from functools import wraps


# EXECUTION -------------

def add_method(cls):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            return func(self, *args, **kwargs)
        setattr(cls, func.__name__, wrapper)
        return wrapper
    
    return decorator


# END -------------------

if __name__ == '__main__':
    pass
