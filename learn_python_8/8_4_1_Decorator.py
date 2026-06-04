import functools
# now.__name__ 'now'
# f.__name__ 'now'
def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print('2026-6-03')
@log1('execute')
def now1():
    print('2026-6-03')


f = now
f()
now1()
